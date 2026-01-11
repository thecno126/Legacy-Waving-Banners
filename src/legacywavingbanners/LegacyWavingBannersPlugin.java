package legacywavingbanners;

import com.fs.starfarer.api.BaseModPlugin;
import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.campaign.FactionAPI;
import lunalib.lunaSettings.LunaSettings;

public class LegacyWavingBannersPlugin extends BaseModPlugin
{
    @Override
    public void onGameLoad(boolean newGame)
    {
        applyHegemonyFlag();
    }

    private void applyHegemonyFlag()
    {
        FactionAPI faction = Global.getSector().getFaction("hegemony");
        String choice = "default";

        // Check if LunaLib is enabled
        if (Global.getSettings().getModManager().isModEnabled("lunalib"))
        {
            choice = LunaSettings.getString("legacywavingbanners", "hegemonyFlag");
        }

        // Set the flag based on user choice
        if ("alt".equals(choice))
        {
            faction.setCustomFlag("graphics/factions/hegemony_alt.png");
        }
        else
        {
            faction.setCustomFlag("graphics/factions/hegemony.png");
        }
    }
}
