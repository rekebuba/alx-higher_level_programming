#include "lists.h"

/**
 * is_palindrome - checks if a liked list is a palindrome
 * @head: a pointer to a linked list
 * the approach i fallowed is that
 * first create a copy the linked list
 * second reverse the copy list
 * third compare the two linked list
 * Return: 0 if it is not, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head, *new_node = NULL, *current = NULL;
	listint_t *node = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
/* creating a new node */
	while (ptr != NULL)
	{
		node->n = ptr->n;
		node->next = NULL;
		if (new_node == NULL)
		{
			new_node = node;
			current = new_node;
		}
		else
		{
			current->next = node;
			current = current->next;
		}
		ptr = ptr->next;
	}
	reverse_node(&new_node);

	listint_t *ptr1 = *head;
	listint_t *ptr2 = new_node;

	while (ptr1 && ptr2)
	{
		if (ptr1->n != ptr2->n)
		{
			return (0);
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	return (1);
}

/**
 * reverse_node - reverse a node
 * @head: the linked list need to be reversed
 * Return: void
 */
void reverse_node(listint_t **head)
{
	listint_t *new_node = *head;
	listint_t *temp1 = NULL;
	listint_t *temp2;

	while (new_node != NULL)
	{
		temp2 = new_node->next;
		new_node->next = temp1;
		temp1 = new_node;
		new_node = temp2;
	}
	*head = temp1;
}
