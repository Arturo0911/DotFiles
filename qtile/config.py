from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import psutil # installed by pip the psutil dependency
import json

mod = "mod4"
terminal = guess_terminal()

keys = [
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
    Key([mod], "m", lazy.spawn("brave")),
    Key([mod], "g", lazy.spawn("thunar")),
    Key([mod], "x", lazy.spawn("zoom")),
    Key([mod], "z", lazy.spawn("postman")),
    Key([mod], "v", lazy.spawn("codium")),
    Key([mod], "t", lazy.spawn("spotify")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "i", lazy.spawn("arduino")),
    Key([mod], "b", lazy.spawn("/opt/Gogland/bin/goland.sh")),
    Key([mod], "s", lazy.spawn("scrot -s -e 'mv ~/Pictures/'")),
    Key([mod, 'shift'], 's', lazy.spawn("scrot")),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "p", lazy.spawn("pycharm")),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

#group_list = ["","","DEV",""]
groups = [Group(i) for i in [
    "","","","ﮧ","", "漣", ""
    ]]
#groups = [__groups[i] for i in __groups]

for i, group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], actual_key, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(actual_key)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(actual_key)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_with=2,
        # margin=10,
        border_focus ="#543470"
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='JetBrains Mono',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def base(fg='text', bg='dark'):
    with open("config.json") as file:
        return {
            'foreground': json.load(file)[fg][0],
            'background': json.load(file)[bg][0]
        }

def separator():
    return widget.Sep(linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        background="fb9f7f",
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg, bg):
    return widget.TextBox(
        # **base(fg, bg),
        foreground=bg,
        # background=bg,
        text="", # Icon: nf-oct-triangle_left
        fontsize=71,
        padding=-12.2
    )



screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(fontsize=25),
                widget.Prompt(),
                widget.WindowName(
                    fontsize=12,
                    font="Hack Nerd Font"
                    ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                powerline(fg="#f1ffff", bg="#fb9f7f"),
                widget.Net(
                        
                        foreground = "#0f101a",
                        background = "#fb9f7f",
                        interface="enp0s25",
                        format = '﬉ {down} ↓↑{up}',
                        padding = 15,
                        fontsize = 15,
                        font="UbuntuMono Nerd Font"
                        ),
                # separator(),
                # widget.Sep(**base(), linewidth=0, padding=5),
                # powerline('color1', 'dark'),
                # powerline(),
                # powerline(fg="#f1ffff", bg="#a151d3"),
                widget.CPU(
                    # foreground= "#069c88",
                    font="UbuntuMono Nerd Font",
                    foreground = "#0f101a",
                    background="#a151d3",
                    format= ' {freq_current}GHz {load_percent}%',
                    padding = 15,
                    fontsize = 15
                ),
                widget.Systray(),
                # powerline(),
                widget.Clock(
                    font="UbuntuMono Nerd Font",
                    format=' %Y-%m-%d %I:%M %p',
                    padding = 15,
                    fontsize = 15,
                    foreground = "#0f101a",
                    background="#0e79b7"
                    ),
                # powerline(),
                # powerline(fg="#f1ffff", bg="#069c88"),
                # widget.Memory(
                #     format = ' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                #     # foreground="#e407eb",
                #     # font = "JetBrainsMono Nerd Font",
                #     font="UbuntuMono Nerd Font",
                #     padding = 15,
                #     fontsize = 13,
                #     #foreground="#f1ffff",
                #     foreground = "#0f101a",
                #     background="#069c88"
                # ),
            ],
            30,
        ),
    ),
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

wmname = "LG3D"


cmd = [
    "setxkbmap latam",
    "feh --bg-fill ~/.config/qtile/vibes.jpg",
    "picom &"
]

for x in cmd:
    os.system(x)
