import re

path = r'C:\Users\hr\OneDrive\Documents\AB fluence website\hr dashboard.html'
content = open(path, 'r', encoding='utf-8').read()

# ── 1. addLeadModal field IDs ──────────────────────────────────────────────
content = content.replace(
    '<input class="form-input" placeholder="e.g. TechPak Solutions">',
    '<input id="lead-name" class="form-input" placeholder="e.g. TechPak Solutions">'
)
content = content.replace(
    '<select class="form-select"><option>E-commerce</option><option>Healthcare</option><option>F&B</option><option>SaaS / Tech</option><option>Real Estate</option><option>Education</option><option>Fashion</option><option>Finance</option><option>Other</option></select>',
    '<select id="lead-industry" class="form-select"><option>E-commerce</option><option>Healthcare</option><option>F&B</option><option>SaaS / Tech</option><option>Real Estate</option><option>Education</option><option>Fashion</option><option>Finance</option><option>Other</option></select>',
    1  # first occurrence only (leads modal)
)
content = content.replace(
    '<input class="form-input" placeholder="Full name">',
    '<input id="lead-contact" class="form-input" placeholder="Full name">'
)
content = content.replace(
    '<input class="form-input" placeholder="City, Country">',
    '<input id="lead-loc" class="form-input" placeholder="City, Country">',
    1  # first occurrence
)
content = content.replace(
    '<select class="form-select"><option>Starter Brand Package</option>',
    '<select id="lead-interest" class="form-select"><option>Starter Brand Package</option>'
)
content = content.replace(
    '<input class="form-input" placeholder="$0">',
    '<input id="lead-val" class="form-input" placeholder="$0">'
)
content = content.replace(
    '<select class="form-select"><option>Inbound</option>',
    '<select id="lead-source" class="form-select"><option>Inbound</option>'
)
print('Lead modal IDs wired')

# ── 2. onboardModal field IDs ──────────────────────────────────────────────
content = content.replace(
    '<input class="form-input" placeholder="Client company">',
    '<input id="ob-name" class="form-input" placeholder="Client company">'
)
# Industry select in onboard modal (second occurrence, after lead's)
content = content.replace(
    '<select class="form-select"><option>E-commerce</option><option>Healthcare</option><option>F&B</option><option>SaaS / Tech</option><option>Real Estate</option><option>Education</option><option>Fashion</option><option>Other</option></select>',
    '<select id="ob-industry" class="form-select"><option>E-commerce</option><option>Healthcare</option><option>F&B</option><option>SaaS / Tech</option><option>Real Estate</option><option>Education</option><option>Fashion</option><option>Other</option></select>',
    1  # first remaining occurrence (after lead industry was replaced)
)
content = content.replace(
    '<input class="form-input" placeholder="Name">',
    '<input id="ob-contact" class="form-input" placeholder="Name">'
)
content = content.replace(
    '<input class="form-input" type="email" placeholder="email@company.com">',
    '<input id="ob-email" class="form-input" type="email" placeholder="email@company.com">'
)
content = content.replace(
    '<input class="form-input" placeholder="City, Country">',
    '<input id="ob-location" class="form-input" placeholder="City, Country">',
    1  # first remaining
)
content = content.replace(
    '<select class="form-select"><option>Starter Brand</option>',
    '<select id="ob-package" class="form-select"><option>Starter Brand</option>'
)
content = content.replace(
    '<input class="form-input" placeholder="Monthly value">',
    '<input id="ob-mrr" class="form-input" placeholder="Monthly value">'
)
content = content.replace(
    'onclick="closeModal(\'onboardModal\');toast(\'Client onboarded successfully\',\'success\')"',
    'onclick="saveNewClient()"'
)
print('Onboard modal IDs wired')

# ── 3. filterProjects uses renderBrandProjects ─────────────────────────────
content = content.replace(
    "  document.querySelectorAll('.project-card').forEach(card => {\n    const match = type === 'all' || card.dataset.type === type;\n    card.style.display = match ? '' : 'none';\n  });",
    "  renderBrandProjects(type);"
)
print('filterProjects updated')

# ── 4. Wire DOMContentLoaded ───────────────────────────────────────────────
content = content.replace(
    "document.addEventListener('DOMContentLoaded', () => {\n  initCharts('command');",
    "document.addEventListener('DOMContentLoaded', () => {\n  loadAll();\n  initCharts('command');"
)
content = content.replace(
    "  // Auto-check Ollama on load\n  checkOllama();",
    "  renderKanban();\n  renderClientTable();\n  renderBrandProjects('all');\n  // Auto-check Ollama on load\n  checkOllama();"
)
print('DOMContentLoaded wired')

# ── Verify ─────────────────────────────────────────────────────────────────
print('body tags:', content.count('<body'))
print('lead-name:', 'id="lead-name"' in content)
print('ob-name:', 'id="ob-name"' in content)
print('loadAll in DOMContent:', 'loadAll();\n  initCharts' in content)
print('renderKanban in DOMContent:', 'renderKanban();\n  renderClientTable' in content)

open(path, 'w', encoding='utf-8').write(content)
print('DONE')
