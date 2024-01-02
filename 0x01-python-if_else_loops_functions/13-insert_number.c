#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *ptr = *head;
	if (node == NULL)
	{
		return (NULL);
	}

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	if (ptr->n >= number)
	{
		node->next = ptr;
		*head = node;
		return (node);
	}

	while (ptr != NULL)
	{
		if (ptr->next == NULL && ptr->n <= number)
		{
			ptr->next = node;
			return (node);
		}
		if (ptr->next->n >= number)
		{
			node->next = ptr->next;
			ptr->next = node;
			break;
		}
		ptr = ptr->next;
	}
	return (node);
}
