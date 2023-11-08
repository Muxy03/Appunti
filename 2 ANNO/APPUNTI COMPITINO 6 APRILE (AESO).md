processi/thread possono cooperare mediante shared memory o explicit messages (Global/Local enviroment)

thread schedule is non-deterministic

![[Schermata del 2023-04-04 20-46-13.png]]

![[Schermata del 2023-04-04 21-45-36.png]]

![[Schermata del 2023-04-04 21-49-38.png]]

![[Schermata del 2023-04-05 10-28-03.png]]

![[Schermata del 2023-04-05 10-31-29.png]]

Mesa:
- Signal puts waiter on ready list
- Signaler keeps lock and processor
- ![[Schermata del 2023-04-05 10-39-06.png]]

Hoare:
- Signal gives processor and lock to waiter
- when waiter finishes, processor/lock given back to signaler
- Nested (impilabile) signal possible 
- ![[Schermata del 2023-04-05 10-37-43.png]]

![[Schermata del 2023-04-05 10-42-31.png]]

Spinlock =  a Lock where the processor waits in a loop for the lock to become free (active waiting!)
-  Assumes lock will be held for a short time 
- Used to protect ready list and to implement locks

![[Schermata del 2023-04-05 10-49-06.png]]

Lock implemetation Linux:
- Fast path = If lock is FREE, and no one is waiting, then TestAndSet
- Slow path = If lock is BUSY or someone is waiting, then see previous slide
- User-level locks:
	- fast path = acquire lock using test&set
	- slow path = system call to kernel, to use kernel lock

![[Schermata del 2023-04-05 10-56-10.png]]

![[Schermata del 2023-04-05 10-58-32.png]]

![[Schermata del 2023-04-05 11-09-13.png]]

Filosofi a Cena -> ogni filosofo necessita 2 bacchette per mangiare, ognuno prende la bacchetta a destra per prima

![[Schermata del 2023-04-05 11-11-40.png]]

metodi per evitare deadlock:
- detect and fix
- static prevention
- Dynamic prevention (banker's algorithm)

![[Schermata del 2023-04-05 11-19-31.png]]

5b pagina 31
