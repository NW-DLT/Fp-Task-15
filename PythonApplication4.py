import json
from typing import Iterable
import numpy as np

with open("in.json", "r") as json_file:
    in_json = json.load(json_file)

def my_max(elem):
    row_index, coln_index = np.where(a == elem)
    row_index = row_index[0]
    coln_index = coln_index[0]
    main_diagonal = np.diagonal(a,coln_index-row_index)
    off_diagonal = np.diagonal(np.flipud(a),coln_index-(len(a)-1-row_index))

    if coln_index-row_index > 0:
        main_diagonal = np.delete(main_diagonal,coln_index-abs(coln_index-row_index))
    else:
        main_diagonal = np.delete(main_diagonal,coln_index)

    if coln_index-(len(a)-1-row_index) >0:
        off_diagonal = np.delete(off_diagonal,coln_index-abs(coln_index-(len(a)-1-row_index)))
    else:
        off_diagonal = np.delete(off_diagonal,coln_index)

    return max(main_diagonal.tolist() + off_diagonal.tolist())


def iterable(x):
    return list(map(my_max,x))


a = np.array(in_json["in"])

a = list(map(iterable,a))


with open('out.json', 'w') as result:
    out = {'result': a}
    json.dump(out, result, indent=2)