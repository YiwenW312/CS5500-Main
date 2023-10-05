**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Draw on Canvas

**Primary Actor**: User

**Goal in Context**: To draw on the canvas in real-time using the mouse.

**Preconditions**: (1) The program is running. (2) The canvas is initialized. (3) A color has been selected.

**Trigger**: User left-clicks and drags the mouse over the canvas.
  
**Scenario**: User places the cursor over the canvas. -> User presses the left mouse button and begins to drag. -> As the mouse is dragged, the canvas updates in real-time, painting the selected color wherever the cursor moves.
 
**Exceptions**: If the mouse is dragged outside the canvas boundary, no drawing should occur outside the canvas.

**Priority**: High-priority.

**When available**: First release.

**Channel to actor**: User communicates through the mouse. The system should acknowledge in real-time, ensuring smooth drawing on the canvas.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Pressure sensitivity and brush sizes might be considered in future versions.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
