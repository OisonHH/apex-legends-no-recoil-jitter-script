function OnEvent(event, arg)
    if event == "PROFILE_ACTIVATED" then
        EnablePrimaryMouseButtonEvents(true)
    end

    if (event == "MOUSE_BUTTON_PRESSED" and arg == 1) then
        is_firing = true
        if IsKeyLockOn("Your desired activation key") then
            repeat
                MoveMouseRelative(-6, 6)
                Sleep(10)
                MoveMouseRelative(6, -6)
                Sleep(10)
            until not IsMouseButtonPressed(1)
        end
        is_firing = false
      end
    end
