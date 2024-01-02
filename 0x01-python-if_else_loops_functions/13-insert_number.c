#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *temp;
	listint_t *ptr = *head;
	if (node == NULL)
	{
		return (NULL);
	}
	while (ptr != NULL)
	{
		if (ptr->n < number && ptr->next->n > number)
		{
			node->n = number;
			temp = ptr->next;
			ptr->next = node;
			node->next = temp;
		}
		ptr = ptr->next;
	}
	return (node);
}
