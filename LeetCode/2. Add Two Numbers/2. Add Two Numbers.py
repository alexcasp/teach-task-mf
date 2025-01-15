# Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа.
# Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру.
# Сложите два числа и верните сумму в виде связанного списка.
# Вы можете предположить, что эти два числа не содержат ведущих нулей, кроме самого числа 0.
# Ввод: l1 = [2,4,3], l2 = [5,6,4]
# Вывод: [7,0,8]
# Объяснение: 342 + 465 = 807.
# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next




