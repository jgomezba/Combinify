from Combinatory.combinatory import Combinatory

def test_order_does_not_matter():
    elements = [1, 2, 3, 4]
    group_size = 2
    order_matters = False
    expected_output = [(2, 4), (1, 2), (3, 4), (1, 4), (2, 3), (1, 3)]
    cmb_class = Combinatory(elements, group_size, order_matters)
    cmb_class.get_groupings()
    result = cmb_class.groups
    assert sorted(result) == sorted(expected_output)

def test_order_matters():
    elements = [1, 2, 3, 4]
    group_size = 2
    order_matters = True
    expected_output = [(2, 4), (1, 2), (2, 1), (3, 4), (4, 1), (3, 1), (4, 3), (1, 4), (4, 2), (2, 3), (3, 2), (1, 3)]
    cmb_class = Combinatory(elements, group_size, order_matters)
    cmb_class.get_groupings()
    result = cmb_class.groups
    assert sorted(result) == sorted(expected_output)
    
    