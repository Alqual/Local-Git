import numpy as np
import os
import json
from hybrid_models import AdaptiveLangevinMemory

def generate_synthetic_data(dim=384):
    np.random.seed(42)
    v_A = np.random.normal(0, 1, dim)
    v_A /= np.linalg.norm(v_A)
    
    noise_pool = []
    for _ in range(10):
        v_n = np.random.normal(0, 1, dim)
        v_n /= np.linalg.norm(v_n)
        noise_pool.append(v_n)
    return v_A, noise_pool

def generate_svg_graph(results, filename="comparison_graph.svg"):
    # Simple SVG Generator for headless environments
    width, height = 800, 400
    padding = 50
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F033FF']
    
    svg = [f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background:#f8f9fa; border-radius:8px;">']
    svg.append('<rect width="100%" height="100%" fill="#ffffff" />')
    svg.append(f'<line x1="{padding}" y1="{height-padding}" x2="{width-padding}" y2="{height-padding}" stroke="black" />')
    svg.append(f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height-padding}" stroke="black" />')
    
    for idx, (name, fidelities) in enumerate(results.items()):
        points = []
        for t, f in enumerate(fidelities):
            if t % 10 == 0: # Downsample for SVG path size
                x = padding + (t / len(fidelities)) * (width - 2*padding)
                y = (height - padding) - (f * (height - 2*padding))
                points.append(f"{x},{y}")
        
        path_data = "M " + " L ".join(points)
        svg.append(f'<path d="{path_data}" fill="none" stroke="{colors[idx % 4]}" stroke-width="2" />')
        svg.append(f'<text x="{padding + 10}" y="{padding + 20 + idx*20}" fill="{colors[idx % 4]}" font-family="Arial" font-size="12">{name}</text>')
        
    svg.append('<text x="400" y="380" text-anchor="middle" font-family="Arial" font-size="14">Turns (1-1000)</text>')
    svg.append('<text x="20" y="200" text-anchor="middle" font-family="Arial" font-size="14" transform="rotate(-90 20,200)">Fidelity (Cosine Sim)</text>')
    svg.append('</svg>')
    
    with open(filename, 'w') as f:
        f.write("\n".join(svg))
    print(f"Graph saved as {filename}")

def run_1000_turn_study():
    DIM = 384
    TURNS = 1000
    v_A, noise_pool = generate_synthetic_data(DIM)
    case_types = ['LINEAR_INSTANT', 'LINEAR_SMOOTH', 'SIGMOID_INSTANT', 'SIGMOID_SMOOTH']
    
    memories = {t: AdaptiveLangevinMemory(DIM, gate_type=t) for t in case_types}
    histories = {t: [] for t in case_types}
    
    print(f"Running 1000-turn simulation...")
    for t in range(1, TURNS + 1):
        if t == 1:
            v_in, score = v_A, 1.0
        else:
            v_in, score = noise_pool[np.random.randint(0, 10)], 0.1
            
        for name, mem in memories.items():
            mem.update(v_in, attention_score=score)
            fidelity = np.dot(mem.state, v_A)
            histories[name].append(fidelity)
            
    for name, hist in histories.items():
        print(f"{name:<15} | Final Fidelity: {hist[-1]:.4f}")
        
    generate_svg_graph(histories)

if __name__ == "__main__":
    run_1000_turn_study()
