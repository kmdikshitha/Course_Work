from collections import defaultdict

def atom_counter(formula: str) -> str:

    def split(formula):
        stack = []
        counter = defaultdict(int)
        i = 0
        
        while i < len(formula):
            if formula[i].isalpha():
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j

                count = 0
                while i < len(formula) and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if element in counter:
                    if count > 0:
                        counter[element] += count
                    else:
                        counter[element] += 1 
                else:
                    if count > 0:
                        counter[element] = count
                    else:
                        counter[element] = 1  


            elif formula[i] == '(': 
                stack.append(counter)
                counter = defaultdict(int)
                i += 1

            elif formula[i] == ')':
                i += 1
                count = 0
                while i < len(formula) and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if count > 0:
                    count = count  
                else:
                    count = 1

                for key in counter:
                    counter[key] *= count
                
                if stack:
                    previous_count = stack.pop()
                    for key, value in counter.items():
                        previous_count[key] += value
                    counter = previous_count

        return counter

    atom_counts = split(formula)

    sorted_atoms = sorted(atom_counts.items())
    output = ''
    for atom, count in sorted_atoms:
        if count > 1:
            output += f"{atom}{count}"
        else:
            output += f"{atom}"

    
    return output

# print(atom_counter("H2O"))            # Output: "H2O"
# print(atom_counter("Mg(OH)2"))        # Output: "H2MgO2"
# print(atom_counter("K4(ON(SO3)2)2"))  # Output: "K4N2O6S4"
# print(atom_counter("C6H12O6"))        # Output: "C6H12O6"
# print(atom_counter("Fe2(SO4)3"))      # Output: "Fe2O12S3"
