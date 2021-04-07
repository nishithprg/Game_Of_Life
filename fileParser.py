
class Parser:
    def __init__(self, input_file):
        self.input_file = input_file
        self.automataType = ''
        self.rows = 0
        self.columns = 0
        self.num_evolutions = 0
        self.initial_grid = []
        self.living_rules = []
        self.dead_rules = []

    def parseInputFile(self):
        with open(self.input_file, encoding='utf8') as f:
            self.automataType = f.readline().strip()
            
            if(self.automataType == '2D'):
                # Parse grid dimensions (same dimensions)
                rows, columns = map(int, f.readline().strip().split(' '))
                self.rows = rows
                self.columns = columns
                # Parse the initial grid
                for i in range(rows):
                    elem = list(map(int, f.readline().strip().split(' '))) 
                    self.initial_grid.append(elem)
            else:
                self.rows = 1
                self.initial_grid = list(map(str, f.readline().strip().split(' ')))
                self.columns = len(self.initial_grid)

            # Parse number of evolutions
            self.num_evolutions = int(f.readline().strip())

            if(self.automataType == '1D'):
                elem = f.readline().strip()
                while(elem != ''):
                    tran, res = elem.split(',')
                    elem = (list(map(str, tran.strip().split(' '))), res.strip())
                    self.living_rules.append(elem)
                    elem = f.readline().strip()
            else:
                elem = f.readline().strip()
                # Parse evolution rules for living cells
                while( elem != 'Z' and elem != ''):
                    # print(elem)
                    tran, res = elem.split(',')
                    # print(tran, res)
                    elem = (list(map(int, tran.strip().split(' '))), int(res)) 
                    self.living_rules.append(elem)
                    elem = f.readline().strip()

                if(elem == 'Z'):
                    elem = f.readline().strip()
                    # Parse evolution rules for dead cells
                    while(elem != ''):
                        tran, res = elem.split(',')
                        elem = (list(map(int, tran.strip().split(' '))), int(res)) 
                        self.dead_rules.append(elem)
                        elem = f.readline().strip()