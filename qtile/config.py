from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
import subprocess
import os

from colors.catppuccin import Catppuccin

mod = "mod4"
modAlt = "mod1"
terminal = guess_terminal()


WIDGET_FONT = "Iosevka Nerd Font"
COLOR = Catppuccin()

APP_AUDIO_SETTINGS = "pavucontrol"



# ██╗░░██╗███████╗██╗░░░██╗██████╗░██╗███╗░░██╗██████╗░
# ██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██║████╗░██║██╔══██╗
# █████═╝░█████╗░░░╚████╔╝░██████╦╝██║██╔██╗██║██║░░██║
# ██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔══██╗██║██║╚████║██║░░██║
# ██║░╚██╗███████╗░░░██║░░░██████╦╝██║██║░╚███║██████╔╝
# ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░╚══╝╚═════╝░
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([modAlt], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], 'Tab', lazy.next_screen(), desc='Next monitor'),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "Escape", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]






# ░██████╗░██████╗░░█████╗░██╗░░░██╗██████╗░░██████╗
# ██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔════╝
# ██║░░██╗░██████╔╝██║░░██║██║░░░██║██████╔╝╚█████╗░
# ██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██╔═══╝░░╚═══██╗
# ╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░░░░░██████╔╝
# ░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░░░░╚═════╝░
groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="q", screen_affinity=0),
    Group(name="w", screen_affinity=0),
    Group(name="e", screen_affinity=0),
    Group(name="1", screen_affinity=1),
    Group(name="2", screen_affinity=1),
    Group(name="3", screen_affinity=1),
    Group(name="4", screen_affinity=1),
    Group(name="5", screen_affinity=1),
]

def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '12345':
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))






# ██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██╗░░░██╗████████╗░██████╗
# ██║░░░░░██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
# ██║░░░░░███████║░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░╚█████╗░
# ██║░░░░░██╔══██║░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░░╚═══██╗
# ███████╗██║░░██║░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░██████╔╝
# ╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░╚═════╝░
layouts = [
    layout.Columns( margin= [10,10,10,10],
        border_focus="#FFF",
	    border_normal='#1F1D2E',
        border_width=2,
    ),

    layout.Max(	border_focus='#FFF',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=2,
    ),
]






# ██████╗░░█████╗░██████╗░
# ██╔══██╗██╔══██╗██╔══██╗
# ██████╦╝███████║██████╔╝
# ██╔══██╗██╔══██║██╔══██╗
# ██████╦╝██║░░██║██║░░██║
# ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
decorations=[RectDecoration(group=True, use_widget_background=True, clip=True, radius=3, filled=True, padding_y=3, padding_x=0)]
decorations_github=[RectDecoration(group=True, use_widget_background=True, clip=True, radius=14,    filled=True)]

widget_defaults = dict(
    font=WIDGET_FONT,
    fontsize=14,
    padding=8,
)

icons_defaults = dict(
    font=WIDGET_FONT,
    fontsize=14,
    padding=10)

main_groupbox = widget.GroupBox(
    active=COLOR.groupbox_active,
    background=COLOR.groupbox_background,
    inactive=COLOR.groupbox_inactive,
    this_screen_border=COLOR.groupbox_this,
    other_screen_border=COLOR.groupbox_other,
    this_current_screen_border=COLOR.groupbox_this_current,
    other_current_screen_border=COLOR.groupbox_other_current,
    highlight_method='line',
    highlight_color=[COLOR.groupbox_this, COLOR.groupbox_this],
    disable_drag=True,
    # hide_unused=True,
    borderwidth=1,
    decorations=decorations,
    padding=12,
    visible_groups=[
        groups[0].name,
        groups[1].name,
        groups[2].name,
    ]
    )

secondary_groupbox = widget.GroupBox(
    active=COLOR.groupbox_active,
    background=COLOR.groupbox_background,
    inactive=COLOR.groupbox_inactive,
    this_screen_border=COLOR.groupbox_this,
    other_screen_border=COLOR.groupbox_other,
    this_current_screen_border=COLOR.groupbox_this_current,
    other_current_screen_border=COLOR.groupbox_other_current,
    highlight_method='line',
    highlight_color=[COLOR.groupbox_this, COLOR.groupbox_this],
    disable_drag=True,
    # hide_unused=True,
    borderwidth=1,
    decorations=decorations,
    padding=12,
    visible_groups=[
        groups[3].name,
        groups[4].name,
        groups[5].name,
        groups[7].name,
    ])

extension_defaults = widget_defaults.copy()

main_top_widgets = [
    
    widget.Spacer(15),

    widget.TextBox("", fontsize=20, foreground="#08F"),

    widget.Spacer(5),

    widget.CurrentLayoutIcon(
        background=COLOR.current_layout.bg,
        foreground=COLOR.current_layout.fg,
        decorations=decorations,
        scale=0.8),

    widget.WindowCount(
        background=COLOR.window_count.bg, 
        foreground=COLOR.window_count.fg, 
        show_zero=True,
        decorations=decorations),

    widget.Spacer(5),

    main_groupbox,

    widget.Spacer(10),

    widget.Prompt(),
    
    # widget.Mpris2(
    #     name="spotify",
    #     display_metadata=['xesam:title', 'xesam:artist'],
    #     scroll_chars=None,
    #     objname="org.mpris.MediaPlayer2.spotify",
    #     scroll_interval=0,
    #     background=COLOR.spotify.bg,
    #     foreground=COLOR.spotify.fg,
    #     fmt='{}   ',
    #     paused_text='   {track}',
    #     mouse_callbacks={
    #         "Button3": lazy.function(go_to_group("8"))
    #     },
    #     decorations=decorations
    # ),

    widget.Spacer(5),

    # widget.Clipboard(
    #     fmt="󰅎  Copied",
    #     max_width=2,
    #     background=COLOR.clipboard.bg,
    #     foreground=COLOR.clipboard.fg,
    #     decorations=decorations,
    #     **widget_defaults),

#     widget.Spacer(),
 
    # widget.Chord(
    #     font="Iosevka NF ", 
    #     background=COLOR.chord.bg, 
    #     foreground=COLOR.chord.fg, 
    #     fmt=(" ") + "{}" + "   Esc -> Cancel"
    # ),
   
    widget.Spacer(),

# # NO
# # #     widget.CPU(
# # #        background=COLOR.cpu.bg,
# # #        foreground=COLOR.cpu.fg,
# # #        decorations=decorations
# # #    ),

# # #    widget.Spacer(5),

# # #    widget.Memory(
# # #        format='RAM {MemUsed: .3f}{mm} / {MemTotal: .3f}{mm}',
# # #        measure_mem='G',
# # #        background=COLOR.ram.bg,
# # #        foreground=COLOR.ram.fg,
# # #        decorations=decorations,
# # #        **widget_defaults),

# # #   widget.Spacer(5),
# # NO

    widget.CheckUpdates(
        display_format="  {updates}",
        colour_have_updates=COLOR.check_updates.fg,
        background=COLOR.check_updates.bg,
        no_update_string="",
        decorations=decorations),

    # widget.Spacer(5),

#     # Internet Widget
#     widget.GenPollText(
#         func=lambda: subprocess.check_output(WIDGET_INTERNET).decode(),
#         update_interval=1, 
#         background=COLOR.Blue,
#         foreground=COLOR.Crust,
#         decorations=decorations,
#         max_chars=20,
#         **widget_defaults
#     ),

    widget.Spacer(5),
    
    widget.Volume(
        fmt="  {}",
        background=COLOR.audio.bg,
        foreground=COLOR.audio.fg, 
        mouse_callbacks={
            "Button3": lazy.spawn(APP_AUDIO_SETTINGS)
        },
        decorations=decorations,
        **widget_defaults),

    # widget.Spacer(5),
    
#     # Battery Widget
#     widget.GenPollText(
#         func=lambda: subprocess.check_output(WIDGET_BATTERY).decode(),
#         update_interval=1, 
#         background=COLOR.battery_icon.bg,
#         foreground=COLOR.battery_icon.fg,
#         decorations=decorations,
#         **icons_defaults
#     ),
    
#     widget.Battery(
#         background=COLOR.battery.bg,
#         foreground=COLOR.battery.fg,
#         low_background=COLOR.battery_low.bg,
#         low_foreground=COLOR.battery_low.fg,
#         low_percentage=0.40,
#         notify_below=20,
#         charge_char="  ",
#         full_char="  ",
#         discharge_char="",
#         unknown_char="? ",
#         show_short_text=False,
#         decorations=decorations,
#         format='{percent:2.0%} {char}',
#         update_interval=2,
#         padding=0
#     ),

    widget.Spacer(5),

    widget.Clock(
        format=f"%H:%M:%S | %d/%m/%y",
        background=COLOR.clock.bg,
        foreground=COLOR.clock.fg,
        decorations=decorations,
        mouse_callbacks={},
        **widget_defaults
    ),

    # widget.Systray(),

    widget.Spacer(10),

#     widget.GithubNotifications(
#         active_colour=COLOR.github_active,
#         inactive_colour=COLOR.github_inactive,
#         error_colour=COLOR.github_error,
#         background=COLOR.github_background,
#         token_file=f"{HOME}/.github-token",
#         icon_size=23,
#         decorations=decorations_github,
#         mouse_callbacks={
#             "Button1": lazy.spawn(GITHUB_NOTIFICATIONS)
#         },
#         padding=2),

    widget.Spacer(25),
]

secondary_top_widgets = [
    widget.Spacer(10),
    
    widget.CurrentLayoutIcon(
        background=COLOR.current_layout.bg,
        foreground=COLOR.current_layout.fg,
        decorations=decorations,
        scale=0.8),

    widget.WindowCount(
        background=COLOR.window_count.bg, 
        foreground=COLOR.window_count.fg, 
        show_zero=True,
        decorations=decorations),

    widget.Spacer(5),

    secondary_groupbox,

    widget.Spacer()
]

bar_style = dict(
    background=COLOR.bar.bg,
    border_color=COLOR.bar.bg,
    margin=[0, 0, 0, 0],
    border_width=0)

main_bar = bar.Bar(widgets=main_top_widgets, size=25, **bar_style)
secondary_bar = bar.Bar(widgets=secondary_top_widgets, size=25, **bar_style)    

screens = [
    Screen(top=main_bar),
    
    Screen(top=secondary_bar),
]






# ██╗░░██╗░█████╗░░█████╗░██╗░░██╗
# ██║░░██║██╔══██╗██╔══██╗██║░██╔╝
# ███████║██║░░██║██║░░██║█████═╝░
# ██╔══██║██║░░██║██║░░██║██╔═██╗░
# ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
# ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
HOME = os.path.expanduser('~')
AUTOSTART = f'{HOME}/.config/qtile/autostart.sh'
@hook.subscribe.startup
def autostart():
    """ Executes a script on qtile startup """
    home = os.path.expanduser(AUTOSTART)
    subprocess.call([home])






# ░█████╗░████████╗██╗░░██╗███████╗██████╗░
# ██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗
# ██║░░██║░░░██║░░░███████║█████╗░░██████╔╝
# ██║░░██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗
# ╚█████╔╝░░░██║░░░██║░░██║███████╗██║░░██║
# ░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
