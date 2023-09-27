#include <iostream>
#include <queue>
using namespace std;

struct ListNode {
    int data;
    ListNode *next;

    ListNode(int data) {
        this->data = data; 
        next = NULL;
    }
};

struct TreeNode {
    int data;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int data) {
        this->data = data; 
        left = NULL;
        right = NULL;
    }
};

TreeNode *constructBinaryTree(ListNode *head) {
    if (head == nullptr) return nullptr;

    queue<TreeNode*> qu;
    TreeNode *root = new TreeNode(head->data);
    qu.push(root);
    ListNode *temp = head;
    temp = temp->next;

    while (!qu.empty && temp != nullptr) { 
        TreeNode *curr = qu.front();
        qu.pop();

        if (temp != nullptr) {
            TreeNode *leftChild = new TreeNode(temp->data);
            curr->left = leftChild;
            qu.push(leftChild);

            temp = temp->next;
        }

        if (temp != nullptr) {
            TreeNode *rightChild = new TreeNode(temp->data);
            curr->right = rightChild;
            qu.push(rightChild);

            temp = temp->next;
        }
    }

    return root;
}

void levelOrderTraversal(TreeNode *root) {
    if (root == nullptr) return;

    queue<TreeNode*> qu;
    qu.push(root);

    while (!qu.empty()) {
        TreeNode *curr = qu.front();
        qu.pop();

        cout << curr->data << " ";

        if (curr->left) {
            qu.push(curr->left);
        }

        if (curr->right) {
            qu.push(curr->right);
        }
    }
}

int main() {
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    TreeNode *root = constructBinaryTree(head);

    cout << "Level Traversal of Binary Tree constructed from Linked List is ";
    levelOrderTraversal(root);
    cout << endl;

    return 0;
}



// ------------------------------------------------------------------------------------------------------------



// Create Linked List from Binary Tree
struct ListNode {
    int data;
    ListNode *next;

    ListNode(int data) {
        this->data = data; 
        next = NULL;
    }
};

struct TreeNode {
    int data;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int data) {
        this->data = data; 
        left = NULL;
        right = NULL;
    }
};

ListNode* createLinkedListFromBinaryTree(TreeNode *root) {
    if (root == nullptr) return nullptr;

    queue<TreeNode*> q;
    ListNode *head = nullptr;
    ListNode *tail = nullptr;
    q.push(root);

    while (!q.empty()) {
        TreeNode *curr = q.front();
        q.pop();

        ListNode *newNode = new ListNode(curr->data);

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }

        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }

    return head;
}

void printLinkedList(ListNode *head) {
    ListNode *current = head;
    while (current != nullptr) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    ListNode *head = createLinkedListFromBinaryTree(root);

    cout << "Linked List from Binary Tree: ";
    printLinkedList(head);

    return 0;
}






