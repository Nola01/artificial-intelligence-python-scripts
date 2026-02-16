""" 
Simple forward chaining
 """

facts = {"A", "B"}

#Rule base
rules = [
    ({"A", "B"}, "C"), #e.g., if A and B are true, then infer C
    ({"C"}, "D"),
    ({"D", "E"}, "F")
]

""" 
set inferred = true in order to start the loop.
assume no facts will be inferred in the iteration, so set inferred to 'False'.
for any pair (condition, conclusion) in rules, if facts are a subset of
the conditions AND the conclusion is not among the facts, add the conclusion
to the facts, then set inferred to 'True' because a new fact was inferred so
we repeat the loop.
 """
def forward_chaining(facts, rules):
    inferred = True

    while inferred:
        inferred = False 
        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion) 
                inferred = True  
                print(f"Inferred: {conclusion}")

    return facts

final_facts = forward_chaining(facts,rules)
print("Final set of facts: ", final_facts)
