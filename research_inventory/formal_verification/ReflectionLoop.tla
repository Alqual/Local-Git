------------------- MODULE ReflectionLoop -------------------
EXTENDS Integers, Sequences

CONSTANT MaxRetries

VARIABLES 
    status,    \* 状態: "IDLE", "WORKING", "PASS", "FAIL_FINAL"
    attempt    \* 試行回数 (1..MaxRetries)

Vars == <<status, attempt>>

\* 初期状態
Init == 
    /\ status = "IDLE"
    /\ attempt = 1

\* 試行開始
Start == 
    /\ status = "IDLE"
    /\ status' = "WORKING"
    /\ attempt' = 1

\* 検証成功 -> 完了
Success == 
    /\ status = "WORKING"
    /\ status' = "PASS"
    /\ attempt' = attempt

\* 検証失敗 -> リトライ
Retry == 
    /\ status = "WORKING"
    /\ attempt < MaxRetries
    /\ status' = "WORKING"
    /\ attempt' = attempt + 1

\* 最大試行到達 -> 最終失敗
GiveUp == 
    /\ status = "WORKING"
    /\ attempt = MaxRetries
    /\ status' = "FAIL_FINAL"
    /\ attempt' = attempt

Next == 
    \/ Start
    \/ Success
    \/ Retry
    \/ GiveUp
    \/ (status \in {"PASS", "FAIL_FINAL"} /\ UNCHANGED Vars)

Spec == Init /\ [][Next]_Vars /\ WF_Vars(Next)

------------------------------------------------------------
\* 不変量 (Invariant)
Invariant == 
    /\ attempt \in 1..MaxRetries
    /\ (status = "PASS" => attempt <= MaxRetries)

\* 停止性 (Liveness)
Termination == <>(status = "PASS" \/ status = "FAIL_FINAL")
============================================================
