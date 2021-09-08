#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a num in a sorted singly linked lst
 * @head: pointer head
 * @number: insert node
 *
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new;
  listint_t *current;
  listint_t *temp;

  current = *head;
  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;
  new->next = NULL;

  if (head == NULL)
    return (new);
  else if (*head == NULL)
    *head = new;
  else if (current->n > number)
    {
      *head = new;
      new->next = current;
    }
  else
    {
      while (current->next != NULL)
	{
	  temp = current;
	  current = current->next;
	  if (current->n > number)
	    {
	      temp->next = new;
	      new->next = current;
	      return (new);
	    }
	}
      current->next = new;
    }
  return (new);
}
