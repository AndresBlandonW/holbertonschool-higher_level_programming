#include "lists.h"

/**
 * print_dlistint - print all elem of list
 * @h: linked list
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		if (h->next == NULL)
			printf("%d\n", h->n);
		else
			printf("%d\n", h->n);
		count++;
		h = h->next;
	}

	return (count);
}
