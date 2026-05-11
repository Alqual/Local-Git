import numpy as np

class SNRMonitor:
    def __init__(self, window_size=20):
        self.window_size = window_size
        self.history = []
    
    def record(self, signal_mag, noise_mag):
        snr = signal_mag / (noise_mag + 1e-9)
        self.history.append(snr)
        if len(self.history) > self.window_size:
            self.history.pop(0)
    
    @property
    def current_snr(self):
        return np.mean(self.history) if self.history else 1.0

class LangevinMemory:
    def __init__(self, dim, mu=0.001, sigma=0.01):
        self.dim = dim
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
        self.monitor = SNRMonitor()

    def update(self, v_in, alpha):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.dim)
        
        # Physics update
        self.state += drift + diffusion + alpha * v_in
        self._normalize()
        
        # Basic monitoring
        self.monitor.record(np.linalg.norm(alpha * v_in), np.linalg.norm(drift + diffusion))

    def _normalize(self):
        norm = np.linalg.norm(self.state)
        if norm > 0: self.state /= norm

class AdaptiveLangevinMemory(LangevinMemory):
    def __init__(self, dim, mu=0.001, sigma=0.01, gate_type='SIGMOID_INSTANT', window=10):
        super().__init__(dim, mu, sigma)
        self.gate_type = gate_type
        self.window = window
        self.sim_history = []
        
    def _get_alpha(self, v_in, attention_score=1.0):
        # Feedback Loop: Saturation Avoidance
        sim = np.dot(self.state, v_in / (np.linalg.norm(v_in) + 1e-9))
        self.sim_history.append(sim)
        if len(self.sim_history) > self.window:
            self.sim_history.pop(0)
            
        current_sim = max(0, sim)
        avg_sim = max(0, np.mean(self.sim_history))
        
        # 4 Gating Strategies
        if self.gate_type == 'LINEAR_INSTANT':
            gate = 1.0 - current_sim
        elif self.gate_type == 'LINEAR_SMOOTH':
            gate = 1.0 - avg_sim
        elif self.gate_type == 'SIGMOID_INSTANT':
            beta = 20
            gate = 1.0 / (1.0 + np.exp(beta * (current_sim - 0.15)))
        elif self.gate_type == 'SIGMOID_SMOOTH':
            beta = 20
            gate = 1.0 / (1.0 + np.exp(beta * (avg_sim - 0.15)))
        else:
            gate = 0.1
            
        alpha = (0.5 * attention_score * gate) + 0.01
        return alpha

    def update(self, v_in, attention_score=1.0):
        alpha = self._get_alpha(v_in, attention_score)
        super().update(v_in, alpha)
        return alpha
