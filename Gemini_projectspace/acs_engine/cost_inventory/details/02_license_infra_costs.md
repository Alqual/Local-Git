# Cost Category 2: Infrastructure & License Management

## Component Mission
To maintain a stable, secure, and collaborative development environment while managing fixed recurring costs.

## Infrastructure Breakdown

### 1. Networking (Tailscale)
- **Role**: Provides the "Virtual LAN" for cross-node SSH.
- **Cost Policy**: Utilizing the Free Tier (Personal) for up to 3 nodes. If the node count exceeds this, the project will transition to the "Starter/Pro" plan.

### 2. Version Control (GitHub)
- **Role**: SSoT for code and mathematical artifacts.
- **Cost Policy**: Free for public repositories. Private repository features (like detailed environment secrets) may require a Pro subscription.

### 3. Compute Resources
- **Allocation**: The Alma node (Main) and Ubuntu node (Compute) are hosted on existing local hardware. 
- **Amortization**: Energy costs and hardware depreciation are tracked as "Implicit Costs" but not charged against the LLM token budget.

## Challenges & Outlook
- **API Quotas**: Google Cloud quotas can limit the number of parallel translation requests.
- **Outlook**: "Multi-Project Balancing". Distributing the API load across multiple Google Cloud projects to leverage free-tier quotas and prevent billing spikes.
