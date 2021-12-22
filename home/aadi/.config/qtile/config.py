# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from libqtile import hook
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import widget
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.client_new
def client_new(client):
    if client.name == 'slack':
        client.togroup('mail')

mod = "mod1"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    Key([mod, "control"], "r", lazy.restart(), desc="Reload the config"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "s", lazy.spawn('systemctl suspend'), desc="Suspend system"),
    # Replaced by dmenu
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn command rompt"),
    # custom applications

    Key([mod, "shift"], "Return", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="🡲",
        background= "#000", #"#15181a",
        foreground= "#AAA",
        selected_background="#8338EC",#"#079822",
        selected_foreground="#fff",
    ))),
    Key([mod], "b", lazy.spawn("vivaldi-stable"), desc="Open browser"),
    Key([mod], "f", lazy.spawn("nautilus"), desc="Open File manager"),
    Key([mod], "s", lazy.spawn("/home/aadi/.scripts/search.sh"), desc="Search"),
    Key([mod], "m", lazy.spawn("evolution"), desc="Mail"),
    Key([], "F2",  lazy.window.toggle_fullscreen(),desc="Toggle Fullscreen"),
    # Key([mod], "space", lazy.spawn("emacs"), desc="Open EMACS"),
    # Screenshot
    Key([mod], "p", lazy.spawn("flameshot gui")),

    # accounting for second monitor
    Key([mod], "i",
        lazy.to_screen(0)),
    Key([mod], "u",
        lazy.to_screen(1))
]

group_names = [
	("code", {}),
	("www", {}),
	("files", {}),
	("pdf", {}),
    ("5", {}),
	("mail", {}),
	("TBD", {}),
	("plan", {})
]


groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i), lazy.group[name].toscreen(),
            desc="Switch to group {}".format(name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(name)),
    ])

layouts_config = {
    'border_focus': '#8338ec',
    'border_normal': '#000000',
    'border_width': 2,
    'margin': 4
}

layouts = [
    layout.Columns(**layouts_config),
    layout.Max(**layouts_config),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2, **layouts_config),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(**layouts_config),
    # layout.MonadWide(),

    # layout.Floating(**layouts_config),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(**layouts_config)
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="hack",
    fontsize=14,
    padding=3,
    background="#000b1e"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(background="#000000", foreground="#FFFFFF"),
                widget.GroupBox(
                    font="Goldman-Sans",
                    foreground="#000000",
                    background="#FFFFFF", 
                    active="#000000",
                    inactive="#AAAAAA",
                    block_highlight_text_color="#FFFFFF",
                    highlight_method="block",
                    other_current_screen_border="#8338ec",
                    other_screen_border="#8338EC",
                    this_current_screen_border="#FF006E",
                    this_screen_border="#FF006E",
                    margin=3,
                    ),
                widget.Prompt(background="#ff006e"),
                widget.WindowName(**widget_defaults),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Pomodoro(
                    color_active='#f3a86f',
                    color_break='#fb5607',
                    color_inactive='#FFFFFF',
                    length_pomodori=90
                ),
                widget.Pomodoro(
                    color_active='#f3a86f',
                    color_break='#fb5607',
                    color_inactive='#FFFFFF',
                    length_pomodori=30
                ),
                widget.CPUGraph(graph_color="#80ffdb", **widget_defaults),
                widget.MemoryGraph(graph_color="#fb5607", type="box", **widget_defaults),
                widget.ThermalSensor(**widget_defaults),
                widget.Net(interface="wlp5s0", format='{down}↓ {up}↑', **widget_defaults),
                widget.Systray(),
                widget.Volume(background="#3a86ff"),
                widget.Clock(format='%Y-%m-%d %a %H:%M')
            ],
            24,
            border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(bottom=bar.Bar([
            widget.CurrentLayout(background="#FFFFFF", foreground="#000000"),
            widget.WindowName(**widget_defaults),
        ],
            24, border_width=[4,4,4,4]))
    # Screen(bottom=bar.Bar(
    #         [
    #             widget.CurrentLayout(background="#000000", foreground="#FFFFFF")
    #         ]
    #     )
    # )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
