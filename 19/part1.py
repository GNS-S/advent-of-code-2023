def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        flows, parts = parse_input(f)

        possible_ops = ['<', '>']
        apply = {
            '<': lambda a, b: a < b,
            '>': lambda a, b: a > b,
        }
        
        total = 0
        for part in parts:
            state = 'in'
            
            while state not in ['A', 'R']:
                flow = flows[state]
                next_state = None

                for step in flow.split(','):
                    if ':' not in step:
                        next_state = step
                    else:
                        rule, on_pass = step.split(':')
                        op = next(op for op in possible_ops if op in rule)
                        attr, val = rule.split(op)
                        required = int(val)

                        if apply[op](part[attr], required):
                            next_state = on_pass

                    if next_state:
                        state = next_state
                        if state == 'A':
                            total += sum(part.values())
                        break

        print(total)

def parse_input(file) -> tuple[dict, list]:
    workflow_lines, part_lines = file.read().strip().split('\n\n')

    flows = {}
    for line in workflow_lines.split('\n'):
        name, rest = line.strip().split('{')
        flow = rest[:-1]
        flows[name] = flow

    parts = [] 
    for line in part_lines.split('\n'):
        attrs = line.strip()[1:-1].split(',')
        part = {}
        for attr in attrs:
            name, value = attr.split('=')
            part[name] = int(value)

        parts.append(part)

    return flows, parts

if __name__ == '__main__':
    main()
