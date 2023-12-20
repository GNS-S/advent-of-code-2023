from collections import deque
from math import prod

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        modules, state = parse_input(f)

        total = { 'L': 0, 'H': 0 }

        for _ in range(1000):
            Q = deque([('button', 'broadcaster', 'L')])

            while Q:
                sender, name, pulse = Q.popleft()
                
                total[pulse] += 1
                
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

        print(prod(total.values()))

def parse_input(file) -> tuple[dict, dict]:
    modules = {}
    state = {}

    for line in file:
        name, outputs = line.strip().split(' -> ')
        if name == 'broadcaster':
            mtype = 'broadcaster'
        else:
            mtype, name = name[:1], name[1:]
        modules[name] = { 'out': outputs.split(', '), 'type': mtype }

    for name in modules:
        mtype = modules[name]['type']
        if mtype == '%':
            state[name] = False
        if mtype == '&':
            state[name] = { m: 'L' for m in modules if name in modules[m]['out'] } 

    return modules, state

if __name__ == '__main__':
    main()
