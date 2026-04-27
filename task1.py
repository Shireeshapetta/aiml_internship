class InterviewFSM:
    def __init__(self, name):
        self.name = name
        self.state = "START"
        self.history = [self.state]

        # Transition rules
        self.transitions = {
            "START": {"begin": "TECH"},
            "TECH": {"pass": "FOLLOW-UP", "fail": "END"},
            "FOLLOW-UP": {"complete": "END"}
        }

    # AI-like evaluation logic
    def evaluate_candidate(self, score):
        if score >= 50:
            return "pass"
        else:
            return "fail"

    # State transition function
    def transition(self, event):

        # Safety check
        if self.state == "END":
            print(f"{self.name}: Interview already finished")
            return

        # Perform transition
        if self.state in self.transitions and event in self.transitions[self.state]:
            prev_state = self.state
            self.state = self.transitions[self.state][event]
            self.history.append(self.state)

            print(f"{self.name}: {prev_state} → {self.state}")
        else:
            print(f"{self.name}: Invalid transition")

    # Run full interview process
    def run_interview(self, tech_score):
        print(f"\n--- Interview Started for {self.name} ---")

        # START → TECH
        self.transition("begin")

        # TECH evaluation
        result = self.evaluate_candidate(tech_score)
        print(f"{self.name}: Technical Score = {tech_score} → {result.upper()}")

        self.transition(result)

        # FOLLOW-UP (if passed)
        if self.state == "FOLLOW-UP":
            print(f"{self.name}: Attending HR round...")
            self.transition("complete")

        print(f"{self.name}: Final State → {self.state}")
        print(f"{self.name}: State History → {self.history}")


# -------------------------------
# Testing with multiple candidates
# -------------------------------

c1 = InterviewFSM("Ravi")
c2 = InterviewFSM("Anjali")

c1.run_interview(75)   # Should pass
c2.run_interview(40)   # Should fail