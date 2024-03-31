class Map:
  '''
  map - map of characters
  revealed - map of whats been revealed
  '''
  _instance = None
  _initialized = False

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    #create the map of characters by reading the text file and the revealed map
    if not Map._initialized:
      file = open("map.txt")
      self._map = []
      self._revealed = []
      for row in file:
        map_list = []
        revealed_list = []
        for item in row:
          if item != ' ' and item != '\n':
            map_list.append(item)
            revealed_list.append(False)
        self._map.append(map_list)
        self._revealed.append(revealed_list)
      Map._initialized = True
      file.close()

  def __getitem__(self, row):
    return self._map[row]

  def __len__(self):
    return len(self._map)

  def show_map(self, loc):
    #use the revealed and character map to show the current discovered map
    result = ''
    for row in range(len(self._map)):
      for column in range(len(self._map[row])):
        if row == loc[0] and column == loc[1]:
          result += '* '
        elif self._revealed[row][column]:
          result += self._map[row][column] + ' '
        else:
          result += 'x '
      result += '\n'
    return result

  def reveal(self, loc):
    #update the revealed map
    self._revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    #update the character map
    self._map[loc[0]][loc[1]] = "n"
