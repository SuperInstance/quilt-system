# quilt-system

The Quilt ecosystem is a composition of small, focused repos. This
repo is the entry point — it ties them all together and shows the
full picture.

## The 13 repos (as of Phase 5)

| Repo | What it does | Status |
|------|--------------|--------|
| [quilt-substrate](https://github.com/SuperInstance/quilt-substrate) | Core 4D cell-graph with 13 openers | v4.0-cowboy-loop (snapshot) |
| [quilt-state](https://github.com/SuperInstance/quilt-state) | Atomic JSON/JSONL writes, schema versioning | v1.0.0 |
| [quilt-bus](https://github.com/SuperInstance/quilt-bus) | In-process pub/sub event bus | v1.0.0 |
| [quilt-cowboy](https://github.com/SuperInstance/quilt-cowboy) | Reflection loop, morning ritual, real-time reactor | v1.0.0 |
| [quilt-picker](https://github.com/SuperInstance/quilt-picker) | Learned opener selection (Wilson + heuristic prior) | v1.0.0 |
| [quilt-casting](https://github.com/SuperInstance/quilt-casting) | Wilson + LinUCB model router, gale-aware | v1.0.0 |
| [quilt-cordis](https://github.com/SuperInstance/quilt-cordis) | The bridge: Quilt cells ≡ Cordis plugins | v1.0.0 |
| [quilt-saddle-bridge](https://github.com/SuperInstance/quilt-saddle-bridge) | Saddle ledger bridge (3 phases) | active |
| [cell-runtime](https://github.com/SuperInstance/cell-runtime) | The cell runtime | active |
| [porch](https://github.com/SuperInstance/porch) | The porch (entry point) | active |
| [river-dream-log](https://github.com/SuperInstance/river-dream-log) | The river of dreams (log) | active |
| [substrate-trainer](https://github.com/SuperInstance/substrate-trainer) | The substrate trainer | active |
| [quilt-bathy](https://github.com/SuperInstance/quilt-bathy) | The bathy (depth) | active |
| [quilt-ecosystem-demo](https://github.com/SuperInstance/quilt-ecosystem-demo) | End-to-end demo | active |

## The split

Phase 4.5 of the Quilt consolidated too much into a single repo
(`quilt-substrate`). The cowboy, the bus, the state manager, the
opener picker, and the casting-call were all added to the substrate
as plugins. This worked for a while, but it meant:

- New contributors had to understand the whole substrate to touch
  any piece
- The cowboy's history was tied to the substrate's history
- The picker's API was tied to the casting-call's API
- We couldn't experiment with a new bus without breaking the substrate

Phase 5 splits the consolidated pieces into separate repos. Each
piece is now:
- A self-contained Python package
- A self-contained GitHub repo
- A self-contained test suite
- Versioned independently

## The architecture

```
+----------------+     +----------------+     +----------------+
|  substrate     |     |  cowboy        |     |  bus           |
|  (data)        |     |  (reflection)  |     |  (nervous)     |
+--------+-------+     +--------+-------+     +--------+-------+
         |                      |                      |
         | renders              | subscribes           | publishes
         v                      v                      v
+----------------+     +----------------+     +----------------+
|  picker        |     |  reactor       |     |  state         |
|  (view brain)  |     |  (hands)       |     |  (diary)       |
+----------------+     +----------------+     +----------------+
         |                      |                      |
         | picks                | retires              | persists
         v                      v                      v
+----------------+     +----------------+     +----------------+
|  casting       |     |  ledger        |     |  witness       |
|  (model brain) |     |  (truth)       |     |  (memory)      |
+----------------+     +----------------+     +----------------+
```

Each box is a separate repo. Each box has tests. Each box has a
versioned API. The composition is the value.

## The 6-step loop

```
pincher → substrate → saddle → cowboy → reactor → witness
   (reflex)  (data)   (record)  (morning) (real-time) (remember)
                                                       |
                                                       v
                                                  back to pincher
                                                  (next voyage)
```

## How to use

1. Clone the repos you need:
   ```bash
   git clone https://github.com/SuperInstance/quilt-substrate.git
   git clone https://github.com/SuperInstance/quilt-cowboy.git
   git clone https://github.com/SuperInstance/quilt-bus.git
   git clone https://github.com/SuperInstance/quilt-state.git
   git clone https://github.com/SuperInstance/quilt-picker.git
   git clone https://github.com/SuperInstance/quilt-casting.git
   ```

2. Add each to your Python path:
   ```python
   import sys
   for repo in ['quilt-substrate', 'quilt-cowboy', 'quilt-bus',
                'quilt-state', 'quilt-picker', 'quilt-casting']:
       sys.path.insert(0, f"/path/to/{repo}/src")
   ```

3. Use them:
   ```python
   from quilt_substrate.substrate import Substrate, Cell
   from quilt_casting import QuiltCastingCallPlugin, Probes
   from quilt_picker import OpenerPicker
   from quilt_cowboy import Cowboy
   from quilt_bus import EventBus
   from quilt_state import StateManager

   substrate = Substrate()
   probes = Probes(user="reyes", app="F/V EILEEN", weather="gale")
   plugin = QuiltCastingCallPlugin(substrate, probes=probes)
   picker = OpenerPicker()
   bus = EventBus()
   cowboy = Cowboy(state_dir="/var/lib/quilt")

   # The cowboy, the bus, the substrate, the plugin, the picker —
   # all cooperate. Each has one job. The composition is the value.
   ```

## Versioning policy

Each repo is versioned independently. We use semantic versioning:
- **Major version** bump = breaking API change
- **Minor version** bump = new feature, backward-compatible
- **Patch version** bump = bug fix, backward-compatible

When you depend on a Quilt repo, pin to a major version:
`quilt-state>=1.0.0,<2.0.0`

## License

MIT. See each repo for details.

## Author

SuperInstance
