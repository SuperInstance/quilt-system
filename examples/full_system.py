"""full_system.py — Use all 5 Quilt repos together.

This example shows how the 5 small repos compose into a single
system. Each repo is imported separately. The composition is the
value.
"""
import sys
import tempfile
from pathlib import Path

# Add all 5 repos to the Python path
REPOS = ['quilt-substrate', 'quilt-cowboy', 'quilt-bus',
         'quilt-state', 'quilt-picker', 'quilt-casting']
for repo in REPOS:
    sys.path.insert(0, f"/workspace/{repo}/src")

# Now use them
from quilt_substrate.substrate import Substrate, Cell
from quilt_casting import QuiltCastingCallPlugin, Probes
from quilt_picker import OpenerPicker
from quilt_cowboy import Cowboy
from quilt_bus import EventBus
from quilt_state import StateManager


def main():
    print("The Quilt ecosystem: 5 repos, 1 system")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as d:
        d = Path(d)

        # 1. Substrate
        substrate = Substrate()
        substrate.add(Cell(address="bathy:0", value=4.2, axes=("lat", "lon")))
        print(f"  Substrate: {len(substrate)} cells")

        # 2. State
        state = StateManager(str(d / "state"))
        state.save_json("config.json", {"version": "1.0.0", "ts": 0.0})
        print(f"  State: {state.list_files()}")

        # 3. Bus
        bus = EventBus()
        received = []
        bus.subscribe("test.event", lambda e: received.append(e))
        bus.publish("test.event", source="example", data={"hello": "world"})
        print(f"  Bus: {len(received)} events received")

        # 4. Picker
        picker = OpenerPicker()
        opener, score, reason = picker.pick("Murmur", "fable_compression")
        print(f"  Picker: {opener} (score={score:.2f}, {reason})")

        # 5. Casting
        probes = Probes(user="reyes", app="F/V EILEEN", weather="gale")
        plugin = QuiltCastingCallPlugin(substrate, probes=probes)
        decision = plugin.decide(opener="tide", kwargs={"role": "sensory_creative"})
        print(f"  Casting: {decision.model} ({decision.rationale[:60]})")

        # 6. Cowboy
        cowboy = Cowboy(state_dir=str(d / "cowboy"))
        from quilt_cowboy import CowboyAction
        cowboy.memory.append(CowboyAction(
            kind="note", target="system", reason="All 5 repos integrated"
        ))
        print(f"  Cowboy: {len(cowboy.memory.actions)} actions, chain valid: {cowboy.memory.verify_chain()[0]}")

    print()
    print("Each piece has one job. The composition is the value.")


if __name__ == "__main__":
    main()
