#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use tauri::{CustomMenuItem, SystemTray, SystemTrayMenu, SystemTrayMenuItem};

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
fn main() {
    let hide_item = CustomMenuItem::new("hide".toString(), "Hide Window");
    let close_item = CustomMenuItem::new("close".toString(), "Close Admin Panel");
    let tray_menu = SystemTrayMenu::new()
        .add_native_item(SystemTrayMenuItem::Separator)
        .add_item(hide_item)
        .add_item(close_item);

    let sys_tray = SystemTray::new().with_menu(tray_menu);

    tauri::Builder::default()
        .system_tray(sys_tray)
        .on_system_tray_event(|app, event| match event {
            SystemTrayEvent::LeftClick {
                position: _,
                size: _,
                ..
            } => {
                println!("system tray received a left click");
            }
            SystemTrayEvent::DoubleClick {
                position: _,
                size: _,
                ..
            } => {
                println!("system tray received a double click");
            }
            SystemTrayEvent::MenuItemClick { id, .. } => match id.as_str() {
                "close" => {
                    std::process::exit(0);
                }
                "hide" => {
                    let window = app.get_window("main").unwrap();
                    window.hide().unwrap();
                }
                _ => {}
            },
            _ => {}
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
