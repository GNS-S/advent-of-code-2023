from part1 import parse_input

from collections import deque
from math import prod, lcm

# The solution assumes and verifies a specific input shape - subgraphs created by fliplop
# chains feeding NAND gates, which are then collected by a single NAND and set to 'rx'.
# A more elegant solution would involve interpreting flipflop chains as bits to determine
# cycle lengths, but it would still be making assumptions about the input 

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        modules, state = parse_input(f)
        final = 'rx'
        final_inputs = [m for m in modules if final in modules[m]['out']]
        assert len(final_inputs) == 1

        final_nand = final_inputs[0]
        assert modules[final_nand]['type'] == '&'

        watch = [m for m in modules if final_nand in modules[m]['out']]
        assert all([modules[m]['type'] == '&' for m in watch])

        seen = {}

        for i in range(1, 10000):
            Q = deque([('button', 'broadcaster', 'L')])

            while Q:
                sender, name, pulse = Q.popleft()
                key = sender, name, pulse, str(state)
                    
                if name not in modules:
                    continue
                    
                module = modules[name]
                outputs = []
                new_pulse = pulse

                match module['type']:
                    case 'broadcaster':
                        outputs = module['out']
                        new_pulse = pulse
                    case '&':
                        if name == final_nand and pulse == 'H' and sender not in seen:
                               seen[sender] = i
                               if all([w in seen for w in watch]):
                                   break

                        outputs = module['out']
                        state[name][sender] = pulse
                        all_h = all([p == 'H' for p in state[name].values()])
                        new_pulse = 'L' if all_h  else 'H'
                    case '%':
                        if pulse == 'L':
                            outputs = module['out']
                            state[name] = not state[name]
                            new_pulse = 'H' if state[name] else 'L'

                for out in outputs:
                    Q.append((name, out, new_pulse))

        print(lcm(*seen.values()))

if __name__ == '__main__':
    main()
