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
# groups = [Group(i) for i in [
#     "","","","", "ﱾ", "漣",""
#     ]]

groups = [Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("ﱾ", layout='monadtall'),
          Group("漣", layout='monadtall'),
          Group("", layout='monadtall')]


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

"""
layout.MonadTall(
        border_with=2,
        # margin=10,
        border_focus ="#543470"
    ),
"""

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.MonadWide(),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    # layout.Tile(),
    layout.TreeTab(
        font="UbuntuMono Nerd Font",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=3,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    layout.Floating(**layout_theme)
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
    fontsize=8,
    padding=2,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()


def base(fg='text', bg='dark'):
    with open("config.json") as file:
        return {
            'foreground': json.load(file)[fg][0],
            'background': json.load(file)[bg][0]
        }


def separator():
    return widget.Sep(linewidth=0, padding=1)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        background="fb9f7f",
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg, bg):
    return widget.TextBox(
        # **base(fg, bg),
        foreground=bg,
        # background=bg,
        text="",  # Icon: nf-oct-triangle_left
        fontsize=71,
        padding=-12.2
    )


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=20,
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
                widget.WindowName(
                    fontsize=10,
                    font="Hack Nerd Font"
                ),
                widget.TextBox(
                    text='',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[3],
                    fontsize=71,
                    padding=-13.5
                ),
                widget.Net(
                    interface="enp0s25",
                    font="UbuntuMono Nerd Font",
                    fontsize=14,
                    format=' ﬉ {down}↓↑{up}',
                    foreground=colors[1],
                    background=colors[3],
                    padding=0,
                    margin=15,
                    margin_y=30,
                    padding_y=2,
                    padding_x=3,
                ),
                # widget.Net(

                #     foreground="#0f101a",
                #     background="#fb9f7f",
                #     interface="enp0s25",
                #     format='﬉ {down} ↓↑{up}',
                #     padding=10,
                #     fontsize=15,
                #     font="UbuntuMono Nerd Font"
                # ),
                widget.CPU(
                    # foreground= "#069c88",
                    font="UbuntuMono Nerd Font",
                    foreground=colors[1],
                    background=colors[5],
                    format=' {freq_current}GHz {load_percent}%',
                    padding=5,
                    fontsize=12
                ),
                widget.Clock(
                    foreground = "#0f101a",
                    background="#0e79b7",
                    format="  %A, %B %d -  %H:%M ",
                    font="Ubuntu Mono Bold Nerd Font",
                    fontsize=10,
                    padding=0,
                    margin=15,
                    margin_y=30,
                    padding_y=2,
                    padding_x=3
                ),
                # widget.Memory(
                #     font="UbuntuMono Nerd Font",
                #     fontsize = 13,
                #     foreground=colors[1],
                #     background=colors[6],
                #     mouse_callbacks={
                #         'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                #     fmt='Mem: {}',
                #     padding=10
                # )
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
    "feh --bg-fill ~/.config/qtile/rick.jpg",
    "picom &"
]

for x in cmd:
    os.system(x)
