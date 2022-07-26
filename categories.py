#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:12:17 2022

@author: martin
"""

MSZoning_types = [('A','Agriculture'),
                  ('C','Commercial'),
                  ('FV', 'Floating Village Residential'),
                  ('I', 'Industrial'),
                  ('RH', 'Residential High Density'),
                  ('RL', 'Residential Low Density'),
                  ('RP', 'Residential Low Density Park'),
                  ('RM', 'Residential Medium Density')]

MSSubClass_types = sorted(
                   [('20', '1-story 1946 & Newer (All styles)'),
                    ('30', '1-story 1945 & Older'),
                    ('40', '1-story w/ finished attic (All ages)'),
                    ('45', '1-1/2 story Unfinished (All ages)'),
                    ('50', '1-1/2 story Finished (All ages)'),
                    ('60', '2-story 1946 & Newer'),
                    ('70', '2-story 1945 & Older'),
                    ('75', '2-1/2 story (All Ages)'),
                    ('80', 'Split or Multi-level'),
                    ('85', 'Split Foyer'),
                    ('90', 'Duplex - All styles and ages'),
                    ('120', '1-story PUD (Planned Unit Development) - 1946 & Newer'),
                    ('150', '1-1/2 story PUD (All Ages)'),
                    ('160', '2-story PUD - 1946 & Newer'),
                    ('180', 'PUD - Multilevel (Incl. split lev/foyer)'),
                    ('190', '2 Family Conversion (All styles and ages)')],
                   key=lambda x: x[1]
                   )

Neighborhood_types = [('Blmngtn', 'Bloomington Heights'),
                 ('Blueste', 'Bluestem'),
                 ('BrDale', 'Briardale'),
                 ('BrkSide', 'Brookside'),
                 ('ClearCr', 'Clear Creek'),
                 ('CollgCr', 'College Creek'),
                 ('Crawfor', 'Crawford'),
                 ('Edwards', 'Edwards'),
                 ('Gilbert', 'Gilbert'),
                 ('IDOTRR', 'Iowa DOT and Rail Road'),
                 ('MeadowV', 'Meadow Village'),
                 ('Mitchel', 'Mitchell'),
                 ('Names', 'North Ames'),
                 ('NoRidge', 'Northridge'),
                 ('NPkVill', 'Northpark Villa'),
                 ('NridgHt', 'Northridge Heights'),
                 ('NWAmes', 'Northwest Ames'),
                 ('OldTown', 'Old Town'),
                 ('SWISU', 'South & West of Iowa State University'),
                 ('Sawyer', 'Sawyer'),
                 ('SawyerW', 'Sawyer West'),
                 ('Somerst', 'Somerset'),
                 ('StoneBr', 'Stone Brook'),
                 ('Timber', 'Timberland'),
                 ('Veenker', 'Veenker')]
