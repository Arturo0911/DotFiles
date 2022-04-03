from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import psutil  # installed by pip the psutil dependency
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
    "", "", "", "", "ﱾ", "漣", ""
]]

# groups = [Group("", layout='monadtall'),
#           Group("", layout='monadtall'),
#           Group("", layout='monadtall'),
#           Group("", layout='monadtall'),
#           Group("ﱾ", layout='monadtall'),
#           Group("漣", layout='monadtall'),
#           Group("", layout='monadtall')]


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

layout_theme = {"border_width": 1,
                "margin": 3,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

# layout.MonadTall(
#     border_with=2,
#     # margin=10,
#     border_focus="#543470"
# ),


"""

# "focus": [
#         "#a151d3",
#         "#a151d3"
#     ]
layout_conf = {
    'border_focus': "#a151d3",
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
"""
layout_conf = {
    'border_focus': "#a151d3",
    'border_width': 1,
    'margin': 4
}


layouts = [
    # layout.Max(),
    layout.MonadTall(
        border_focus="#a151d3",
        border_width=2
    ),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


widget_defaults = dict(
    font='JetBrains Mono',
    fontsize=15,
    padding=2,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()


# config settings
def load_colors():
    with open("config.json") as f:
        return json.load(f)


def base(fg='text', bg='dark'):
    return {
        'foreground': load_colors()[fg],
        'background': load_colors()[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(
#                     font="Ubuntu Bold",
#                     fontsize=18,
#                     margin_y=2,
#                     margin_x=0,
#                     padding_y=2,
#                     padding_x=3,
#                     borderwidth=3,
#                     active=colors[2],
#                     inactive=colors[7],
#                     rounded=False,
#                     highlight_color=colors[1],
#                     highlight_method="line",
#                     this_current_screen_border=colors[6],
#                     this_screen_border=colors[4],
#                     other_current_screen_border=colors[6],
#                     other_screen_border=colors[4],
#                     foreground=colors[2],
#                     background=colors[0]
#                 ),
#                 widget.TextBox(
#                     text='|',
#                     font="Ubuntu Mono",
#                     background=colors[0],
#                     foreground='474747',
#                     padding=2,
#                     fontsize=14
#                 ),
#                 # widget.Prompt(),
#                 # separator(),
#                 widget.WindowName(
#                     fontsize=10,
#                     font="Hack Nerd Font"
#                 ), #icon(bg="color4", text=' '),
#                 # widget.TextBox(
#                 #     # background="#fb9f7f",
#                 #     foreground="#fb9f7f",
#                 #     fontsize=45,
#                 #     text="",
#                 #     padding=0
#                 # ),
#                 widget.Net(
#                     interface="enp0s25",
#                     format='﬉ {down}↓↑{up}',
#                     padding=7,
#                     # background="#fb9f7f",
#                     foreground="#fb9f7f",
#                     #fontsize = 14,
#                     font="Agave Nerd Font",
#                     fontsize=13,
#                     # font="UbuntuMono Nerd Font"
#                 ),
#                 widget.CPU(
#                     # foreground= "#069c88",
#                     font="UbuntuMono Nerd Font",
#                     foreground=colors[7],
#                     # background=colors[1],
#                     format=' {freq_current}GHz {load_percent}%',
#                     padding=5,
#                     fontsize=13
#                 ),
#                 widget.Systray(),
#                 widget.Clock(
#                     foreground="#0e79b7",
#                     # background="#0e79b7",
#                     font="UbuntuMono Nerd Font",
#                     format=' %Y-%m-%d %I:%M %p',
#                     padding=15,
#                     fontsize=13,
#                 ),
#                 # widget.Memory(
#                 #     font="UbuntuMono Nerd Font",
#                 #     fontsize = 13,
#                 #     foreground=colors[1],
#                 #     background=colors[6],
#                 #     mouse_callbacks={
#                 #         'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
#                 #     fmt='Mem: {}',
#                 #     padding=10
#                 # )
#             ],
#             21,
#         ),
#     ),
# ]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=18,
                    margin_y=2,
                    margin_x=0,
                    padding_y=2,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[7],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[6],
                    other_screen_border=colors[4],
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),
                # widget.Prompt(),
                # widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(
                    fontsize=10,
                    font="Hack Nerd Font"
                ),
                widget.Systray(),
                widget.Net(
                    interface="enp0s25",
                    format='﬉{down}↓↑{up}',
                    padding=7,
                    # background="#fb9f7f",
                    foreground="#fb9f7f",
                    #fontsize = 14,
                    font="Agave Nerd Font",
                    fontsize=13,
                    # font="UbuntuMono Nerd Font"
                ),
                widget.CPU(
                    foreground="#069c88",
                    format=' {freq_current}GHz {load_percent}%',
                    padding=3,
                    fontsize=13,
                    font="UbuntuMono Nerd Font",
                ),
                widget.Clock(
                    foreground="#0e79b7",
                    # background="#0e79b7",
                    font="UbuntuMono Nerd Font",
                    format=' %Y-%m-%d %I:%M %p',
                    padding=15,
                    fontsize=13,
                ),
                # widget.Memory(
                #     #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                #     foreground="#e407eb",
                #     font="JetBrainsMono Nerd Font",
                #     padding=3,
                #     fontsize=11
                # ),
            ],
            21,
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
    "feh --bg-fill ~/.config/qtile/arch.png",
    "picom &"
]

for x in cmd:
    os.system(x)

