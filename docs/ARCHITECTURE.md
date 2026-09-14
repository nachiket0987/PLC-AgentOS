# System Architecture Document — PLC-AgentOS

**Project Name:** PLC-AgentOS  
**Author:** Nachiket Gadilohar  

---

## 1. Architecture Layout
- **CodeGen Agent**: LLM agent fine-tuned on IEC 61131-3 code patterns.
- **Verifier Agent**: Formulates safety propositions and verifies via Z3 Theorem Prover.
- **Knowledge RAG**: Vector index over industrial automation standards.
