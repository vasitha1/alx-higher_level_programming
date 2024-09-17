#include "lists.h"
#include <stddef.h>
#include <stddef.h>

/**
 * is_palindrome - Function that chech if a linked list is a palindrome
 * @head: Pointer to head
 *
 * Return: 1 if a palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	if (*head == NULL || head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
