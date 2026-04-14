# ================================
# PROJECT INTRO PAGE (NAME FIRST)
# ================================

import matplotlib.pyplot as plt

plt.figure(figsize=(12,7))
plt.axis('off')

# ================================
# YOUR NAME (FIRST & BIGGEST)
# ================================

plt.text(0.48, 0.78, "AYESHA",
         fontsize=30, fontweight='bold',style='italic',
         color='#FF1493', ha='center')

plt.text(0.52, 0.72, " ANSARI",
         fontsize=30, fontweight='bold',style='italic',
         color='#00BFFF', ha='center')

# ================================
# PROJECT TITLE
# ================================

plt.text(0.5, 0.60, "Unemployment Analysis With Python",
         fontsize=20, ha='center')

plt.text(0.5, 0.53, "Using Python",
         fontsize=16, ha='center')

# ================================
# INTERNSHIP DETAILS
# ================================

plt.text(0.5, 0.42, " Oasis Infobyte|AICTE Internship Program",
         fontsize=12, ha='center')

plt.text(0.5, 0.37, "Task 2",
         fontsize=12, ha='center')

# ================================
# TOOLS USED
# ================================

plt.text(0.5, 0.28, "Python | Pandas | Matplotlib | Seaborn",
         fontsize=10, ha='center')

# ================================
# EXTRA LINE (UNIQUE TOUCH)
# ================================

plt.text(0.5, 0.18, "Data Science Project",
         fontsize=11, ha='center', style='italic')

plt.text(0.5, 0.10, "Prepared by Ayesha Ansari",
         fontsize=10, ha='center')
plt.show()