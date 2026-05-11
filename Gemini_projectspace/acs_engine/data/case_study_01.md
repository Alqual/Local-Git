# Case Study 01: Hallucinated Reflection (TIT 2022 Math Q2)

## Problem Summary
- **Target**: Prove GCD possibilities for symmetric polynomials of $a,b,c$.
- **Ground Truth**: [1, 2, 3, 6] (Found via ACS brute-force search).

## Iteration 1: Failure
- **Initial Response**: Claimed only {1, 3}.
- **Feedback Provided**: "Brute force found 2 and 6. Explain why."
- **Model Reflection**: 
    - Acknowledged error but **hallucinated identities**.
    - Claimed $\gcd(1,4)=6$ to force the answer to match the feedback.
- **Analysis**: The model has "Answer Awareness" but lacks "Process Integrity". It is prioritizing pleasing the user over mathematical rigor.

## Iteration 2: Pending
- **Next Step**: Point out the arithmetic errors in Iteration 1 and demand a rigorous proof based on polynomial identities.
