def read_file(filename):
  new_list = []
  file = open(filename, "r")
  for line in file:
    line_parts = line.strip().split(",")
    for p in line_parts:
      new_list.append(p)
  return new_list


if __name__ == "__main__":
  my_list = read_file("names_and_numbers.txt")
  my_counts = count_names(my_list)
  print(my_counts)
  print(len(my_counts))
  print(find_name(my_counts, "Adriana"))
  print(find_name(my_counts, "Maria"))
  print(get_most_common_name(my_counts))
  