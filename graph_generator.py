from typing import TYPE_CHECKING
from sortedcontainers import SortedDict
from alpha_miner import AlphaMiner

if TYPE_CHECKING:
    from fastapi import UploadFile

def generate_graph(file: "UploadFile"):
    traces = SortedDict()
    contenu = file.file.read().decode("utf-8")
    events = contenu.split("\n")
    for event in events:
        case_id, activity = event.split(',')
        if case_id not in traces:
            traces[case_id] = []
        traces[case_id].append(activity)

    Alph = AlphaMiner(traces)

    Alph.getInitialTransitions()
    Alph.getFinalTransitions()
    Alph.getTransitions()
    Alph.extractRelations()

    Alph.computePairs()
    Alph.extract_maximal_pairs()
    Alph.add_places()
    Alph.extract_PetriNet()
    try:
        Alph.show(model="petrinet")
    except FileNotFoundError:
        pass
