import re

path = r'C:\Users\hr\OneDrive\Documents\AB fluence website\hr dashboard.html'
content = open(path, 'r', encoding='utf-8').read()

# ─────────────────────────────────────────────
# 1. Replace hardcoded kanban with dynamic container
# ─────────────────────────────────────────────
old_kanban_start = '      <div class="kanban">\n\n        <!-- New -->'
old_kanban_end = '      </div>\n    </div>\n\n    <!-- ══════════ CLIENTS ══════════ -->'
new_kanban = '      <div class="kanban" id="kanban-board"></div>\n    </div>\n\n    <!-- ══════════ CLIENTS ══════════ -->'

s = content.find(old_kanban_start)
e = content.find(old_kanban_end) + len(old_kanban_end)
if s == -1: print('ERROR: kanban start not found')
else:
    content = content[:s] + new_kanban + content[e:]
    print('Kanban replaced')

# ─────────────────────────────────────────────
# 2. Replace hardcoded clients tbody with dynamic
# ─────────────────────────────────────────────
old_tbody_start = '          <tbody>'
old_tbody_end   = '          </tbody>\n        </table>'
s = content.find(old_tbody_start)
e_raw = content.find(old_tbody_end, s)
if s == -1: print('ERROR: tbody start not found')
elif e_raw == -1: print('ERROR: tbody end not found')
else:
    e = e_raw + len(old_tbody_end)
    content = content[:s] + '          <tbody id="clients-tbody"></tbody>\n        </table>' + content[e:]
    print('Clients tbody replaced')

# ─────────────────────────────────────────────
# 3. Replace hardcoded brand project grid with dynamic
# ─────────────────────────────────────────────
old_grid_start = '      <!-- Project Cards -->\n      <div class="project-grid" id="brandProjectGrid">'
# Find end: next </div> that closes the grid, then the g21 section starts
# We'll find the closing tag by looking for the pattern after the grid
s = content.find(old_grid_start)
if s == -1: print('ERROR: project grid start not found')
else:
    # Find the closing of the project grid - it's followed by g21 section
    marker_after = '\n      <div class="g21">'
    e2 = content.find(marker_after, s)
    if e2 == -1: print('ERROR: g21 marker not found')
    else:
        # Replace everything from grid start to g21
        new_grid = '      <!-- Project Cards -->\n      <div class="project-grid" id="brandProjectGrid"></div>\n'
        content = content[:s] + new_grid + content[e2:]
        print('Brand project grid replaced')

# ─────────────────────────────────────────────
# 4. Update onboard modal submit button
# ─────────────────────────────────────────────
content = content.replace(
    "onclick=\"closeModal('onboardModal');toast('Client onboarded! Welcome email sent.','success')\"",
    "onclick=\"saveNewClient()\""
)
print('Onboard submit wired')

# ─────────────────────────────────────────────
# 5. Update add lead modal submit button
# ─────────────────────────────────────────────
content = content.replace(
    "onclick=\"closeModal('addLeadModal');toast('Lead added to pipeline','success')\"",
    "onclick=\"saveNewLead()\""
)
print('Add lead submit wired')

# ─────────────────────────────────────────────
# 6. Update lead detail save button (move stage)
# ─────────────────────────────────────────────
content = content.replace(
    "onclick=\"closeModal('leadDetailModal');toast('Lead updated','success')\"",
    "onclick=\"saveLeadUpdate()\""
)
print('Lead update wired')

# ─────────────────────────────────────────────
# 7. Update new brand project submit
# ─────────────────────────────────────────────
content = content.replace(
    "onclick=\"closeModal('newBrandProjectModal');toast('Brand project created','success')\"",
    "onclick=\"saveNewBrandProject()\""
)
print('New brand project wired')

# ─────────────────────────────────────────────
# 8. Update schedule post submit
# ─────────────────────────────────────────────
content = content.replace(
    "onclick=\"closeModal('newPostModal');toast('Post scheduled','success')\"",
    "onclick=\"saveScheduledPost()\""
)
print('Schedule post wired')

# ─────────────────────────────────────────────
# 9. Update command center quick actions
# ─────────────────────────────────────────────
# Wire the quick action buttons in command center to real actions
content = content.replace(
    "onclick=\"toast('Add new lead','info')\"",
    "onclick=\"go('leads',document.querySelector('.nav[onclick*=\\'leads\\']'));setTimeout(()=>openModal('addLeadModal'),200)\""
)
content = content.replace(
    "onclick=\"toast('Add new client','info')\"",
    "onclick=\"go('clients',document.querySelector('.nav[onclick*=\\'clients\\']'));setTimeout(()=>openModal('onboardModal'),200)\""
)
content = content.replace(
    "onclick=\"toast('Create proposal','info')\"",
    "onclick=\"openModal('proposalModal')\""
)
print('Command center quick actions wired')

open(path, 'w', encoding='utf-8').write(content)
print('DONE. File written.')
