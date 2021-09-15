#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - function that checks a singly linked list is a palindrome
 * @head: Head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
  int len = 0, i = 0, count;
  listint_t *current = *head, *final = *head;

  if (head == NULL)
    return (1);

  while (final->next != NULL)
    {
      final = final->next;
      len++;
    }

  if (len % 2 != 0 && len > 1)
    return (0);

  while (len - i >= i)
    {
      final = current;
      count = i;
      while (count < len - i)
	{
	  final = final->next;
	  count++;
	}
      if (current->n != final->n)
	return (0);
      current = current->next;
      i++;
    }
  return (1);
}
