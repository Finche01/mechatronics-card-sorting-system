# Maintenance Guide - Automated Card Sorting System

## Table of Contents
1. [Maintenance Schedule](#maintenance-schedule)
2. [Timing Belt and Pulley System](#timing-belt-and-pulley-system)
3. [Pneumatic System](#pneumatic-system)
4. [Electrical Components](#electrical-components)
5. [Sensor Calibration](#sensor-calibration)
6. [Lubrication](#lubrication)
7. [Maintenance Log](#maintenance-log)

---

## Maintenance Schedule

### Daily (Before Each Operation)
- [ ] Visual inspection of cables and connections
- [ ] Clean suction cup with isopropyl alcohol
- [ ] Check vacuum hose for kinks or damage
- [ ] Verify E-stop functionality
- [ ] Clear workspace of debris

### Weekly
- [ ] Inspect timing belts for tension and wear
- [ ] Check limit switch operation
- [ ] Clean camera lens
- [ ] Verify vacuum pressure (-20 to -40 kPa)
- [ ] Inspect drag chains for cable stress

### Monthly
- [ ] Full belt tension check and adjustment
- [ ] Lubricate linear rails (X, Y, Z axes)
- [ ] Clean photoelectric sensor lens
- [ ] Inspect pressure switch calibration
- [ ] Check all electrical connections for tightness
- [ ] Verify motor coupling set screws

### Quarterly (Every 3 Months)
- [ ] Deep clean all mechanical components
- [ ] Inspect relay contacts for wear/discoloration
- [ ] Replace vacuum filter if equipped
- [ ] Calibrate vision system templates
- [ ] Test all safety interlocks
- [ ] Backup PLC program and Node-RED flows

### Annually
- [ ] Replace timing belts (preventive)
- [ ] Replace worn linear bearings
- [ ] Inspect motor brushes (if brushed motors)
- [ ] Replace suction cup
- [ ] Full electrical system inspection
- [ ] Relay replacement evaluation

---

## Timing Belt and Pulley System

### Overview
The X and Y axes use GT2 timing belts with 20-tooth pulleys. Proper tension is critical for accurate motion and prevents slippage.

### Belt Specifications
- **Type**: GT2 (2mm pitch)
- **Width**: 6mm
- **Pulley**: 20 teeth
- **Expected Life**: 2000-5000 hours depending on conditions

### Weekly Inspection Checklist

**Visual Inspection**:
- [ ] No fraying or damaged teeth
- [ ] No glazing (shiny surface from slippage)
- [ ] No cracks or splits
- [ ] Uniform wear pattern
- [ ] No debris in belt teeth

**Operational Check**:
- [ ] No unusual vibration during motion
- [ ] No slipping sounds
- [ ] Consistent speed profile
- [ ] No belt jumping on pulley

### Belt Tension Check

**Proper Tension Indicators**:
- Belt deflects 1-2mm when pressed with 5N force at midspan
- No visible sag when motors are disabled
- Smooth motion without jerking

**Too Loose**:
- Symptoms: Positional errors, motor skipping, belt slapping sound
- Risk: Inaccurate positioning, missed steps

**Too Tight**:
- Symptoms: Excessive motor current, bearing noise, rapid wear
- Risk: Premature bearing failure, motor overload

### Belt Tensioning Procedure

**⚠️ WARNING**: Disconnect power before adjusting belts

1. **Prepare System**
   - Power OFF main breaker
   - Remove any cards from workspace
   - Access belt tensioner mechanism

2. **X-Axis Belt Adjustment**
   ```
   Location: Right side of gantry frame
   Tensioner: Screw-type idler pulley
   
   - Loosen tensioner lock nut
   - Turn adjustment screw clockwise to increase tension
   - Check tension with deflection test
   - Tighten lock nut when satisfied
   ```

3. **Y-Axis Belt Adjustment**
   ```
   Location: Rear of gantry frame
   Tensioner: Screw-type idler pulley
   
   - Follow same procedure as X-axis
   - Both Y-axis belts should have equal tension
   ```

4. **Verification**
   - Power ON system
   - Home all axes
   - Run jogging test in all directions
   - Verify no unusual sounds or vibrations
   - Check position repeatability

### Belt Replacement

**When to Replace**:
- Visible teeth damage
- Cracks or fraying
- Glazing from slippage
- >5000 operating hours
- Persistent positioning errors after tension adjustment

**⚠️ IMPORTANT**: Do NOT cut and resize belts. Replace with new belt of correct length.

**Replacement Procedure**:

1. **Order Correct Belt**
   - Measure old belt length or count teeth
   - Order GT2 belt, 6mm width, correct length
   - Have spare on hand before starting

2. **Remove Old Belt**
   - Power OFF and disconnect
   - Release all tension
   - Remove from pulleys
   - Inspect pulleys for wear

3. **Install New Belt**
   - Route through pulley system
   - Ensure teeth fully engage pulleys
   - No twists in belt path
   - Apply moderate initial tension

4. **Calibrate**
   - Follow tensioning procedure above
   - Run extensive motion tests
   - Verify positioning accuracy
   - Log replacement in maintenance record

---

## Pneumatic System

### Vacuum System Overview
- **Vacuum Motor**: Continuous duty, oil-less pump
- **Reservoir**: 15 oz capacity
- **Operating Range**: -20 to -40 kPa
- **Runtime**: ~6 minutes per charge

### Daily Maintenance

**Visual Check**:
- [ ] No air leaks (listen for hissing)
- [ ] Reservoir pressure gauge readable
- [ ] Solenoid clicking when activated
- [ ] Suction cup clean and undamaged

**Suction Cup Cleaning**:
```
Materials: Isopropyl alcohol 70%, lint-free cloth

1. Power OFF system or engage E-stop
2. Dampen cloth with isopropyl alcohol
3. Wipe suction cup surface thoroughly
4. Remove any card fibers or dust
5. Allow to air dry (30 seconds)
6. Test vacuum seal on flat surface
```

### Weekly Maintenance

**Pressure Verification**:
1. With reservoir charged, observe gauge
2. Should read -20 to -40 kPa
3. If below -20 kPa, run vacuum motor
4. If doesn't hold pressure, check for leaks

**Leak Detection**:
```
Method: Soapy water test

1. Mix dish soap with water
2. Apply to all connections with brush
3. Activate vacuum
4. Look for bubbles indicating leaks
5. Tighten fittings or replace if damaged
```

### Monthly Maintenance

**Solenoid Valve Inspection**:
- [ ] Valve body clean and dry
- [ ] Electrical connections secure
- [ ] Coil not overheating during operation
- [ ] No stuck plunger (listen for crisp click)

**Filter Replacement** (if equipped):
1. Locate inline filter in vacuum line
2. Unscrew filter housing
3. Replace element with compatible type
4. Reassemble and test for leaks

### Vacuum Motor Maintenance

**Operating Hours**: Log hours for replacement planning

**Inspection**:
- [ ] Motor runs smoothly without excessive vibration
- [ ] No unusual sounds (grinding, squealing)
- [ ] Intake filter clean (if equipped)
- [ ] Motor body not excessively hot (>50°C)

**Replacement Indicators**:
- Reduced vacuum generation
- Excessive noise
- Overheating
- >2000 operating hours

---

## Electrical Components

### Relay Maintenance

**Overview**:
The system uses electromechanical relays for switching vacuum solenoid and other loads. Rated for ~100,000 cycles.

**Estimated Replacement Schedule**:
```
Usage Pattern: 4.5 cards/min × 60 min × 8 hr/day = ~2,160 cycles/day
Relay Life: 100,000 cycles ÷ 2,160 cycles/day = ~46 days

Recommendation: Inspect monthly, replace quarterly or at 80,000 cycles
```

### Monthly Relay Inspection

**Visual Check**:
- [ ] No discoloration on relay body
- [ ] No burning smell
- [ ] Contact area not blackened
- [ ] Mounting secure, no vibration

**Operational Check**:
- [ ] Crisp clicking sound when switching
- [ ] No hesitation or chatter
- [ ] Load operates reliably
- [ ] No arcing visible/audible

**Warning Signs**:
- Intermittent operation
- Delayed switching
- Contacts welded (relay won't open)
- Visible sparking

### Relay Replacement Procedure

**⚠️ WARNING**: High voltage may be present. Only qualified personnel.

1. **De-energize System**
   - Power OFF main breaker
   - Verify no voltage with multimeter
   - Lock out/tag out if required

2. **Document Wiring**
   - Take photo of connections
   - Label wires before removal
   - Note relay model number

3. **Remove Old Relay**
   - Disconnect all wiring
   - Remove mounting screws
   - Extract relay from panel

4. **Install New Relay**
   - Verify exact replacement (coil voltage, contact rating)
   - Mount securely
   - Reconnect wiring per documentation
   - Double-check polarity on DC coils

5. **Test**
   - Restore power
   - Manually trigger relay from PLC
   - Verify load operates correctly
   - Monitor for first 10 cycles

### Wire Connection Inspection

**Monthly Check**:
- [ ] Terminal screws tight (use torque screwdriver)
- [ ] No frayed or exposed conductors
- [ ] Cable ties secure but not over-tight
- [ ] Drag chain cables not stressed
- [ ] Connectors fully seated

**Troubleshooting Intermittent Issues**:
1. Wiggle test - gently move wires while operating
2. Thermal cycling - run system, let cool, run again
3. Check for cold solder joints on PCBs
4. Inspect crimp connections for looseness

---

## Sensor Calibration

### Photoelectric Sensor (Z-Axis Proximity)

**Purpose**: Slows Z-axis descent near card surface

**Monthly Calibration Check**:

1. **Sensitivity Test**
   ```
   Setup: Place white card on table at camera station
   
   - Manually jog Z-axis downward slowly
   - Note height when sensor activates (LED on)
   - Should trigger 5-10mm above card surface
   - Adjust sensitivity pot if outside range
   ```

2. **Adjustment Procedure**
   - Locate sensitivity potentiometer on sensor
   - Turn clockwise to decrease range (activate closer)
   - Turn counter-clockwise to increase range
   - Test multiple card colors (red, black, white)
   - Set to reliably detect all card types

3. **Verification**
   - Run 10 pick-and-place cycles
   - Z-axis should slow smoothly before contact
   - No overshoot or hard contact
   - Consistent behavior across all tests

### Limit Switches

**Monthly Verification**:

1. **X-Axis Limit**
   - Manually jog to home position
   - Verify switch clicks before physical stop
   - LED indicator should illuminate
   - PLC should halt motion

2. **Y-Axis Limit**
   - Repeat test for Y-axis
   - Check both front and rear limits if equipped

3. **Z-Axis Limit**
   - Jog Z upward to maximum height
   - Verify upper limit switch activation

**Adjustment**:
- Switches should activate 1-2mm before physical end of travel
- Loosen mounting, reposition if needed
- Tighten securely after adjustment

### Pressure Switch (Vacuum Verification)

**Calibration**:
```
Purpose: Confirms card pickup has sealed

1. Check switch activation pressure (typically -15 kPa)
2. Should close contact when vacuum >15 kPa
3. If unreliable, adjust setpoint screw
4. Test with actual card pickup
```

---

## Lubrication

### Linear Rails (X, Y, Z Axes)

**Lubricant**: Light machine oil or recommended rail lubricant  
**Frequency**: Monthly or every 200 operating hours

**Procedure**:

1. **Clean Rails**
   - Wipe rails with lint-free cloth
   - Remove dust and debris
   - Isopropyl alcohol for stubborn residue

2. **Apply Lubricant**
   ```
   X-Axis Rails:
   - Apply 2-3 drops per rail at multiple points
   - Manually move carriage back and forth
   - Spread oil evenly along travel
   
   Y-Axis Rails:
   - Same procedure as X-axis
   
   Z-Axis Lead Screw:
   - Apply light grease to threads
   - Rotate screw to distribute
   - Wipe excess to prevent debris accumulation
   ```

3. **Verify**
   - Motion should feel smooth, no resistance
   - No squeaking or binding
   - Run motion tests to verify

**⚠️ WARNING**: Over-lubrication attracts dust. Use sparingly.

### Motor Couplings

**Inspection**: Check for looseness or wear  
**Tightening**: Verify set screws are secure  
**Replacement**: If visible wear or backlash detected

---

## Maintenance Log

### Sample Log Entry

```
Date: 2026-03-15
Technician: J. Park
Hours: 247.5

Maintenance Performed:
✓ Cleaned suction cup
✓ Inspected X/Y belt tension - within spec
✓ Lubricated Y-axis rails
✓ Tested all limit switches - functional
✓ Verified vacuum pressure: -32 kPa

Issues Found:
- Photoelectric sensor chatter intermittent
- Adjusted sensitivity from 70% to 60%
- Issue resolved

Next Actions:
- Monitor photoelectric performance
- Belt replacement due in ~30 days

Parts Used:
- Isopropyl alcohol: 50ml
- Machine oil: 10ml

Next Scheduled: 2026-03-22
```

### Maintenance Tracking Spreadsheet

Create a log with columns:
- Date
- Operator/Technician
- Operating Hours
- Tasks Completed
- Issues Found
- Parts Replaced
- Next Service Date

---

## Consumable Parts List

### Regular Replacement Items

| Item | Part Number | Replacement Interval | Cost (Est.) |
|------|-------------|---------------------|-------------|
| GT2 Belt (X-axis) | Custom length | 12 months / 2000 hrs | $15 |
| GT2 Belt (Y-axis) | Custom length | 12 months / 2000 hrs | $15 |
| Suction Cup | Generic 20mm | 12 months | $5 |
| Vacuum Relay | Phoenix PLC-RPT | 3 months / 80k cycles | $25 |
| Linear Bearings | LM8UU | 24 months | $20/set |
| Limit Switches | V-156-1C25 | As needed | $10 each |

### Recommended Spare Parts

Keep on hand to minimize downtime:
- (2) GT2 belts (X and Y length)
- (1) Suction cup
- (2) Relays (vacuum and auxiliary)
- (4) Limit switches
- (1) Photoelectric sensor
- (1) Pressure switch

---

## Troubleshooting Common Issues

### Gradual Position Drift

**Cause**: Belt stretch or slip  
**Solution**: Check and adjust belt tension

### Vacuum Pickup Degradation

**Cause**: Dirty suction cup, low pressure  
**Solution**: Clean cup, recharge reservoir, check for leaks

### Inconsistent Vision Classification

**Cause**: Dirty camera lens, lighting changes  
**Solution**: Clean lens, verify consistent lighting

### Relay Failure

**Cause**: End of life (cycle count)  
**Solution**: Replace relay, log in maintenance record

---

## Contact for Technical Support

**Project Team**:
- Joshua Craven: jcraven@myseneca.ca | 647-248-7322
- Jae Park: jpark83@myseneca.ca | 647-500-4630

---

**Document Version**: 1.0  
**Last Updated**: March 2026  
**Prepared by**: J. Craven, J. Park
