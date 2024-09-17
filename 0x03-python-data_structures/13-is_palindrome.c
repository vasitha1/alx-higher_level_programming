#include "lists.h"

/**
 * is_palindrome - Function that chech if a linked list is a palindrome
 * @head: Pointer to head
 *
 * Return: 1 if a palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);

	while (*head->next->next != NULL)
	{
		if (*head->next->n + *head->n != *head->next->next->n)
			return (0);
		*head->next->next = head->next->next->next;
	}
	return (1)
}
