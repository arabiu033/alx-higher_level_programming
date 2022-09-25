#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: thie linked list
 * Return: 1 true
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail, *rev, *new;
	int sig;

	rev = *head;
	if (!rev || !rev->next)
		return (1);

	tail = malloc(sizeof(listint_t));
	tail->n = rev->n;
	tail->next = NULL;

	while (rev->next)
	{
		rev = rev->next;
		new = malloc(sizeof(listint_t));
		new->n = rev->n;
		new->next = tail;
		tail = new;
	}

	rev = *head;
	new = tail;
	while (rev)
	{
		sig = rev->n == tail->n;
		if (!sig)
			break;
		rev = rev->next;
		tail = tail->next;
	}

	free_listint(new);
	if (sig)
		return (1);
	return (0);
}
