Start off with why need async await, lets do a pyscript example
Start with a viztrace of a regular program and a async equivelenent.
And show the two graphs as a description

(it's not actually paralell, its still just one program)
so it's switching back and forth, see if you can see the two things
the semiparallelo
the and then in one line

and show how even sleeps can be errored
and why does this matter- just to show that even the most
innocent functiosn can throw errors, and for this example maybe no
big deal, but on bigger projects with more users, this errors from
nowhere can lead to a lot of delays if we are not conscious of it

then lets talk about things going in parallel
is it truly paralell? it is.

lets look at gather
but what if we have an error? how do we want to handle it

show the gather strategy
- errors, cancelling
  (what about collect errors)
  (what about cancel tasks)
  (do you have the results still if the error gets thrown? no?)

show the task group strategy
  - using try/except, you have to for awaits
  - or, how do we avoid awaits (gather does that)
  - what about error groups (does it work with lists?)

so now, tasks, and coroutines are done

let's talk about futures- low level

lets talk about gil

orphan tasks





asyncio mugs
3 types of awaitables
error groups
useful API (to_thread, TaskGroup, gather)
proper order of checking to avoid an error

- we have hand draw flamegraphs
- we can export generated ones
- we can execute python
- we still need to tell how it looks with threading
- maybe networks
from pyvis.network import Network
import networkx as nx

G = nx.gn_graph(10)

net = Network(notebook=False, directed=True)
net.from_nx(G)
net.show("network.html")

    (async () => {{
      const viz = new Viz();
      const svg = await viz.renderSVGElement(`{dot}`);
      document.getElementById('dag').appendChild(svg);
    }})();
