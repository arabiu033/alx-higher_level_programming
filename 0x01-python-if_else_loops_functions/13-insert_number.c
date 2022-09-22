#include "lists.h"

/**
 * insert_node - insert a new node in a sorted linked list
 * @head: the linked list
 * @number: the new node to add
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new, *next, *prev;

  new = malloc(sizeof(listint_t));
  new->n = number;

  prev = *head;
  next = prev ? prev->next : NULL;

  if (!next)
    {
      if (prev && prev->n > number)
	{
	  new->next = prev;
	  *head = new;
	}
      else
	{
	  new->next = prev->next;
	  prev->next = new;
	}
      return (new);
    }

  while (prev && next)
    {
      if (prev->n < number && next->n > number)
	{
	  new->next = next;
	  prev->next = new;
	  return (new);
	}
      prev = next;
      next = next->next;

      if (!next)
	{
	  if (prev->n > number)
	    new->next = prev;
	  else
	    {
	      new->next = prev->next;
	      prev->next = new;
	    }
	  return (new);
	}
    }
  new->next = NULL;
  *head = new;
  return (new);
}
