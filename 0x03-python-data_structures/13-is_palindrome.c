#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks a singly linked list is a palindrome
 * @head: list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
  int len = 0, i = 0, j;
  listint_t *current = *head, *second = *head;

  if (head == NULL)
    return (1);

  while (second->next != NULL)
    {
      len++;
      second = second->next;
    }

  current = *head;
  while (len - i >= i)
    {
      second = current;
      for (j = 0; j < len; j++)
        {
	  second = second->next;
        }
      if (current->n != second->n)
	return (0);
      current = current->next;
      i++;
    }
  return (1);
}
