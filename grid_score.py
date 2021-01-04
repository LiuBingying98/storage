if __name__ == "__main__":
    with open("dock_47_957.out", "r") as f:
        index = []
        grid_score = []
        for line in f:
            if line.startswith("Molecule:"):
                index.append(int(line.split(" ")[-1]))
            elif "Grid_Score" in line:
                grid_score.append(float(line.split(" ")[-1]))
        for i, s in zip(index, grid_score):
            print(i, " "*10, s)
