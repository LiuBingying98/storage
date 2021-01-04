#split 1000 molecules into 100 each file and delete designated molecules
filename = "1000_charged.mol2"

def flush(div, index):
    with open("output/{}.txt".format(index), "w+") as outf:
        outf.writelines(div)

def load(filename):
    all_mol = []
    curr = ""
    count = 0
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("@<TRIPOS>MOLECULE"):
                if curr != "":
                    all_mol.append((count, curr))
                    count += 1
                    curr = ""
            if line.startswith("*****"):
                line = str(count + 1) + "\n"
            curr += line
    if curr != "":
        all_mol.append((count, curr))
    return all_mol

# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    all_mol = load(filename)
    mol_count = len(all_mol)
    print("load {} mol from file.".format(mol_count))
    deleted_index = [46, 78, 82, 103, 105, 118, 178, 181, 188, 190, 219, 224, 254, 287, 320, 321, 
    351,360, 444, 460, 480, 490, 518, 529, 530, 573, 574, 575, 577, 578, 579, 580, 581, 583, 585,
    625, 651, 669, 676, 683, 705, 706, 708, 709, 713, 716, 737, 808, 812, 887, 892, 897, 924, 956]
    divided = list(chunks(all_mol, 100))
    print("divided into {} lists.".format(len(divided)))
    # print(divided[0])
    for chunk in divided:
        list(map(lambda x: print(x[0], end=" "), chunk))
        print()
    filtered = list(map(lambda x: list(filter(lambda elem: elem[0] not in deleted_index, x)), divided))
    for chunk in filtered:
        list(map(lambda x: print(x[0], end=" "), chunk))
        print()
    for i, div in enumerate(filtered):
        flush(list(map(lambda elem: elem[1], div)), i)

