# Flattening a Linked List

def sortedMerge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    res = None

    if head1.data < head2.data:
        res = head1
        head1.bottom = sortedMerge(head1.bottom, head2)     
    else:
        res = head2
        head2.bottom = sortedMerge(head1, head2.bottom)
        
    res.next = None
    return res


def flatten(root):
    if root is None:
        return None
    
    root.next = flatten(root.next)

    root = sortedMerge(root, root.next)

    return root
