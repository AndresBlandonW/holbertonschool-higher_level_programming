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
  int len = 0, i = 0, j;
  listint_t *current, *second = *head;

  if (head == NULL)
    return (1);

  while (second->next != NULL)
    {
      len++;
      second = second->next;
    }

  while (i != len / 2)
    {
      current = *head;
      second = *head;
      for (j = 0; j < i; j++)
        {
	  current = current->next;
        }
      for (j = 0; j < len - (i + 1); j++)
        {
	  second = second->next;
        }
      if (current->n != second->n)
        {
	  return 0;
        }
      else
        {
	  i++;
        }
    }
 
  return 1;
}
