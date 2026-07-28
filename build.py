#!/usr/bin/env python3
"""Capital Sawmill site generator — builds static pages with shared header/footer."""
import os, pathlib

SITE = pathlib.Path('/root/capital-sawmill/site')

PHONE_DISPLAY = "(518) 479-0729"
PHONE_TEL = "tel:5184790729"
EMAIL = "Steven@CapitalSawmill.com"
ADDRESS = "4119 US HIGHWAY 20. NASSAU, NY 12123"

SVG_PHONE = '<svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M493.4 24.6l-104-24c-11.3-2.6-22.9 3.3-27.5 13.9l-48 112c-4.2 9.8-1.4 21.3 6.9 28l60.6 49.6c-36 76.7-98.9 140.5-177.2 177.2l-49.6-60.6c-6.8-8.3-18.2-11.1-28-6.9l-112 48C3.9 366.5-2 378.1.6 389.4l24 104C27.1 504.2 36.7 512 48 512c256.1 0 464-207.5 464-464 0-11.2-7.7-20.9-18.6-23.4z"/></svg>'
SVG_MARKER = '<svg aria-hidden="true" viewBox="0 0 384 512" fill="currentColor"><path d="M172.268 501.67C26.97 291.031 0 269.413 0 192 0 85.961 85.961 0 192 0s192 85.961 192 192c0 77.413-26.97 99.031-172.268 309.67-9.535 13.774-29.93 13.773-39.464 0zM192 272c44.183 0 80-35.817 80-80s-35.817-80-80-80-80 35.817-80 80 35.817 80 80 80z"/></svg>'
SVG_ENVELOPE = '<svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M502.3 190.8c3.9-3.1 9.7-.2 9.7 4.7V400c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V195.6c0-5 5.7-7.8 9.7-4.7 22.4 17.4 52.1 39.5 154.1 113.6 21.1 15.4 56.7 47.8 92.2 47.6 35.7.3 72-32.8 92.3-47.6 102-74.1 131.6-96.3 154-113.7zM256 320c23.2.4 56.6-29.2 73.4-41.4 132.7-96.3 142.8-104.7 173.4-128.7 5.8-4.5 9.2-11.5 9.2-18.9v-19c0-26.5-21.5-48-48-48H48C21.5 64 0 85.5 0 112v19c0 7.4 3.4 14.3 9.2 18.9 30.6 23.9 40.7 32.4 173.4 128.7 16.8 12.2 50.2 41.8 73.4 41.4z"/></svg>'
SVG_CLOCK = '<svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm57.1 350.1L224.9 294c-3.1-2.3-4.9-5.9-4.9-9.7V116c0-6.6 5.4-12 12-12h48c6.6 0 12 5.4 12 12v137.7l63.5 46.2c5.4 3.9 6.5 11.4 2.6 16.8l-28.2 38.8c-3.9 5.3-11.4 6.5-16.8 2.6z"/></svg>'
SVG_FB = '<svg aria-hidden="true" viewBox="0 0 320 512" fill="currentColor"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg>'
SVG_IG = '<svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg>'
SVG_LI = '<svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg>'
SVG_CHEVRON = '<svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor"><path d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z"/></svg>'
SVG_TRUCK = '<svg aria-hidden="true" viewBox="0 0 640 512" fill="currentColor"><path d="M624 352h-16V243.9c0-12.7-5.1-24.9-14.1-33.9L494 110.1c-9-9-21.2-14.1-33.9-14.1H416V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48v320c0 26.5 21.5 48 48 48h16c0 53 43 96 96 96s96-43 96-96h128c0 53 43 96 96 96s96-43 96-96h48c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zM160 464c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm320 0c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm80-208H416V144h44.1l99.9 99.9V256z"/></svg>'

GLYPHS = {
  'tree': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M36.87,36.426c-1.453.569-3.13.892-4.88.892-1.734,0-3.395-.317-4.839-.875l-2.658,22.202c-.086.721.477,1.355,1.203,1.355h2.524l.66-9.94c.04-.55.52-.97,1.06-.93.55.04.97.51.94,1.06l-.65,9.81h3.54l-.14-5.71c-.01-.55.43-1.01.98-1.02h.02c.54,0,.99.43,1,.97l.14,5.76h2.535c.726,0,1.288-.634,1.203-1.354l-2.638-22.22Z"/> <path d="M47.638,27.023c1.684-1.46,2.739-3.517,2.739-5.804,0-4.288-3.693-7.778-8.333-7.991,0-.02.003-.039.003-.059,0-5.064-4.498-9.169-10.047-9.169s-10.047,4.105-10.047,9.169c0,.02.003.039.003.059-4.64.213-8.333,3.703-8.333,7.991,0,2.287,1.055,4.345,2.739,5.804-3.311,1.571-5.577,4.724-5.577,8.366,0,5.208,4.625,9.429,10.331,9.429h3.017l1.032-8.614c.028-.232.107-.448.209-.652-.432-.276-.837-.572-1.185-.903-.4-.38-.417-1.013-.037-1.414.382-.399,1.014-.417,1.414-.037,1.397,1.327,3.799,2.119,6.424,2.119s5.025-.792,6.423-2.119c.4-.379,1.033-.363,1.414.037.38.4.363,1.033-.037,1.414-.338.321-.731.609-1.148.878.107.205.187.426.215.662l1.024,8.629h3.002c5.706,0,10.331-4.222,10.331-9.429,0-3.641-2.265-6.795-5.577-8.366Z"/> </svg>',
  'crane': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M12,44c-4.418,0-8,3.582-8,8s3.582,8,8,8,8-3.582,8-8-3.582-8-8-8ZM12,56.926c-2.716,0-4.926-2.209-4.926-4.926s2.21-4.925,4.926-4.925c.553,0,1,.448,1,1s-.447,1-1,1c-1.613,0-2.926,1.312-2.926,2.925s1.312,2.926,2.926,2.926,2.926-1.312,2.926-2.926c0-.552.447-1,1-1s1,.448,1,1c0,2.716-2.21,4.926-4.926,4.926Z"/> <path d="M59.838,50.39h-15.808c-.55,0-1-.45-1-1s.45-1,1-1h15.102c-1.32-2.603-4.015-4.39-7.133-4.39H17.975c2.438,1.826,4.025,4.727,4.025,8s-1.588,6.175-4.026,8h34.026c4.418,0,8-3.582,8-8,0-.551-.056-1.09-.162-1.61ZM39.166,55.253h-13.977c-.553,0-1-.448-1-1s.447-1,1-1h13.977c.553,0,1,.448,1,1s-.447,1-1,1Z"/> <path d="M19.155,5h25.689c.553,0,1-.448,1-1s-.447-1-1-1h-25.689c-.553,0-1,.448-1,1s.447,1,1,1Z"/> <path d="M31,24.59v17.41h2v-17.41l14.324,17.41h2.581s-16.103-19.587-16.103-19.587c1.561-.694,2.656-2.254,2.656-4.07,0-2.114-1.479-3.889-3.458-4.344v-3.289h2.76c1.1,0,2-.9,2-2v-1.71h-11.52v1.71c0,1.1.9,2,2,2h2.76v4.176c0,.552.447,1,1,1,1.355,0,2.458,1.103,2.458,2.458s-1.103,2.458-2.458,2.458-2.458-1.103-2.458-2.458c0-.552-.447-1-1-1s-1,.448-1,1c0,1.816,1.095,3.375,2.656,4.07l-16.103,19.587h2.581s14.324-17.41,14.324-17.41Z"/> </svg>',
  'firewood': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M12,44c-4.418,0-8,3.582-8,8s3.582,8,8,8,8-3.582,8-8-3.582-8-8-8ZM12,56.925c-2.716,0-4.925-2.209-4.925-4.925s2.209-4.925,4.925-4.925c.552,0,1,.448,1,1s-.448,1-1,1c-1.613,0-2.925,1.312-2.925,2.925s1.312,2.925,2.925,2.925,2.925-1.312,2.925-2.925c0-.552.448-1,1-1s1,.448,1,1c0,2.716-2.209,4.925-4.925,4.925Z"/> <path d="M16.628,42h9.509c-.651-.5-1.012-.898-1.012-.898-1.582-1.821-2.429-4.272-2.145-6.859.24-2.186,1.247-4.102,2.723-5.509.432-.412,1.146-.17,1.198.425.097,1.115.598,2.51,2.455,2.714,0,0,2.551.28,3.302-3.635.239-1.248.503-3.573.677-5.247.076-.735,1.011-1.011,1.471-.434,4.672,5.859,5.568,9.752,5.568,9.752.417,1.212.58,2.532.43,3.89-.253,2.309-1.27,4.466-2.941,5.801h9.529c1.308-2.188,2.165-4.669,2.426-7.309.56-5.658-1.518-10.845-5.151-14.478,0,0-7.667-6.762.135-14.701.555-.565.145-1.518-.647-1.52-3.727-.011-11.214,1.136-13.348,10.173,0,0-.709,3.603-3.778,3.066-2.113-.37-2.731-3.173-2.886-5.361-.062-.879-1.2-1.211-1.738-.513-9.237,11.987-8.286,21.51-8.286,21.51,0,3.337.918,6.459,2.509,9.133Z"/> <path d="M22.01,60h-4.02c.76-.57,1.44-1.25,2.01-2.01.57.76,1.25,1.44,2.01,2.01Z"/> <path d="M17.99,44h4.02c-.76.57-1.44,1.25-2.01,2.01-.57-.76-1.25-1.44-2.01-2.01Z"/> <path d="M28,44c-4.418,0-8,3.582-8,8s3.582,8,8,8,8-3.582,8-8-3.582-8-8-8ZM28,56.925c-2.716,0-4.925-2.209-4.925-4.925s2.209-4.925,4.925-4.925c.552,0,1,.448,1,1s-.448,1-1,1c-1.613,0-2.925,1.312-2.925,2.925s1.312,2.925,2.925,2.925,2.925-1.312,2.925-2.925c0-.552.448-1,1-1s1,.448,1,1c0,2.716-2.209,4.925-4.925,4.925Z"/> <path d="M50.85,50.39c-.55,0-1-.45-1-1s.45-1,1-1h8.283c-1.32-2.603-4.014-4.39-7.133-4.39h-18.01c2.43,1.82,4.01,4.73,4.01,8s-1.58,6.18-4.01,8h18.01c4.42,0,8-3.58,8-8,0-.552-.056-1.09-.162-1.61h-8.988ZM48.989,55.252h-6.799c-.552,0-1-.447-1-1s.448-1,1-1h6.799c.552,0,1,.447,1,1s-.448,1-1,1Z"/> </svg>',
  'saw': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M45.72,53.65c-.21.05-.41.07-.62.07-1.41,0-2.6-1.06-2.75-2.47l-.22-1.98-1.96.44c-.2.04-.41.07-.61.07-1.42,0-2.6-1.06-2.76-2.47l-.22-1.99-1.95.44c-.2.05-.41.07-.62.07-1.19,0-2.22-.75-2.6-1.84-3.25.51-17.51,2.49-27.41-.67v12.58c8.19-1.19,13.09-3.74,13.15-3.77,6.44-4.04,13.67-4.05,13.98-4.03,8.67-.34,9.74,5.06,9.78,5.28.43,2.43-1,4.97-2.22,6.62h8.48c.48-1.28,1.4-4.15,1.45-7.14-.63.24-1.28.43-1.94.58l-.96.21Z"/> <path d="M38.94,53.74c-.03-.15-.9-3.92-7.78-3.64-.12,0-7.01,0-13.01,3.76-.29.15-5.43,2.84-14.15,4.05v.678c0,.78.632,1.412,1.412,1.412h30.708c1.27-1.39,3.19-4.18,2.82-6.26Z"/> <path d="M31.11,42l-.07-.63-1.95.45c-.21.04-.41.07-.62.07-1.41,0-2.6-1.06-2.75-2.47l-.22-1.99-1.96.44c-.2.05-.41.07-.61.07-1.33,0-2.45-.93-2.72-2.21H5.41c-.78,0-1.41.63-1.41,1.41v4.06c9.35,3.28,23.9,1.3,27.11.8Z"/> <path d="M58.59,35.73h-10.12c.64.26,1.31.57,1.98.91,4.3,2.18,7.53,5.17,9.55,8.82v-8.32c0-.78-.63-1.41-1.41-1.41Z"/> <path d="M47.06,37.33l7.53,9.2c.34.41.49.93.44,1.46-.05.53-.31,1.02-.72,1.35l-1.11.91c-.8.66-1.67,1.23-2.59,1.71.14,3.18-.71,6.27-1.31,8.04h9.29c.78,0,1.41-.63,1.41-1.41v-7.54c-1.78-7.85-8.08-11.8-12.94-13.72Z"/> <path d="M19.786,30.045c-.18,0-.36-.011-.54-.035l-2.813-.364.184,1.662c.051.459.49.771.94.669l3.293-.748c.45-.102.889.21.94.669l.371,3.356c.051.459.49.771.94.669l3.293-.748c.45-.102.889.21.94.669l.372,3.356c.051.459.49.771.94.669l3.293-.748c.45-.102.889.21.94.669l.372,3.356c.051.459.49.771.94.669l3.293-.748c.45-.102.889.21.94.669l.371,3.356c.051.459.49.771.94.669l3.293-.748c.45-.102.889.21.94.669l.372,3.356c.051.459.49.771.94.669l.963-.219c2.087-.474,4.036-1.427,5.693-2.782l1.112-.91-21.839-26.69c-.245.718-.674,1.382-1.303,1.897l-7.449,6.095c-.75.614-1.697.952-2.666.952Z"/> <path d="M11.223,26.348c.357.436.867.72,1.426.792l6.853.887c.603.078,1.212-.096,1.682-.481l7.449-6.095c.944-.773,1.083-2.164.311-3.109l-11.354-13.876c-.629-.768-1.856-.55-2.181.388l-1.521,4.389-7.419,6.071c-1.414,1.157-1.622,3.241-.465,4.655l5.219,6.379ZM10.522,17.196l6.323-5.174c.756-.619,1.871-.507,2.49.249l1.307,1.598c.619.756.507,1.871-.249,2.49l-6.323,5.174c-.756.619-1.871.507-2.49-.249l-1.307-1.598c-.619-.756-.507-1.871.249-2.49Z"/> </svg>',
  'wheelsaw': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <g> <path d="M31.13,46.61c8.67-.34,9.74,5.06,9.78,5.28.43,2.43-1,4.97-2.22,6.62h8.48c.84-2.28,3.09-9.55-.62-13.67-.07-.08-3.47-3.98-14.49-2.45-.69.12-17.07,2.95-28.06-.56v12.58c8.19-1.19,13.09-3.74,13.15-3.77,6.44-4.04,13.67-4.05,13.98-4.03Z"/> <path d="M38.94,52.25c-.03-.15-.9-3.92-7.78-3.64-.12,0-7.01,0-13.01,3.76-.29.15-5.43,2.84-14.15,4.05v.678c0,.78.632,1.412,1.412,1.412h30.708c1.27-1.39,3.19-4.18,2.82-6.26Z"/> <path d="M60,49.56v7.54c0,.78-.63,1.41-1.41,1.41h-9.29c1.07-3.14,2.88-10.4-1.22-14.96-.16-.2-4.01-4.85-16.33-3.14-.18.03-17.25,2.98-27.75-.7v-4.06c0-.78.63-1.41,1.41-1.41h36.1c2.7.48,15.8,3.43,18.49,15.32Z"/> <path d="M58.59,34.24c.78,0,1.41.63,1.41,1.41v8.32c-2.02-3.65-5.25-6.64-9.55-8.82-.67-.34-1.34-.65-1.98-.91h10.12Z"/> </g> <path d="M45.05,32.24c.2-.9.3-1.81.3-2.73,0-7.35-5.98-13.33-13.33-13.33s-13.33,5.98-13.33,13.33c0,.92.1,1.84.3,2.73h-10.64c.02-.03.05-.06.08-.09l3.32-2.91-2.42-3.7c-.23-.33-.29-.74-.18-1.11.11-.39.37-.71.73-.89l4-1.9-1.27-4.25c-.11-.39-.06-.8.16-1.14.23-.34.58-.57.97-.61l4.43-.61.19-4.45c.02-.42.22-.79.54-1.04.33-.25.76-.34,1.16-.25l4.37,1.04,1.95-4.06c.19-.37.52-.65.94-.73.09-.03.2-.04.3-.04.32,0,.62.1.85.3l3.55,2.79,3.55-2.8c.33-.26.74-.36,1.15-.26.42.08.76.36.94.74l1.95,4.04,4.37-1.03c.42-.1.83,0,1.16.25.33.25.52.62.54,1.03l.21,4.46,4.41.61c.4.05.75.27.97.62.22.33.27.74.16,1.13l-1.27,4.25,4,1.9c.36.18.62.5.73.88s.05.79-.18,1.12l-2.42,3.7,3.32,2.91c.04.03.07.06.09.1h-10.65Z"/> <path d="M32.02,18.18c-6.26,0-11.33,5.07-11.33,11.33,0,.94.12,1.86.34,2.73h7.3c-.57-.76-.91-1.71-.91-2.73,0-2.54,2.06-4.6,4.6-4.6s4.6,2.06,4.6,4.6c0,1.02-.34,1.97-.91,2.73h7.3c.22-.87.34-1.79.34-2.73,0-6.26-5.07-11.33-11.33-11.33Z"/> </svg>',
  'truck': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M59.434,26.457l-5.826-12.343c-.54-1.051-1.622-1.712-2.803-1.712h-11.734c-.727,0-1.317.59-1.317,1.317v25.594h-7.259v-2h5.259v-4.017h-5.255v-2h5.255v-4.017h-5.251v-2h5.251v-4.017h-5.247v-2h5.247v-4.017h-5.243v-1.252c0-1.255-1.017-2.273-2.272-2.273s-2.273,1.018-2.273,2.273v1.252s-10.455,0-10.455,0v-1.252c0-1.255-1.017-2.273-2.272-2.273s-2.273,1.018-2.273,2.273v1.252s-6.966,0-6.966,0v4.017h6.97v2s-4.661,0-4.661,0v4.017h4.665v2s-6.974,0-6.974,0v4.017h6.978v2s-4.669,0-4.669,0v4.017h4.673v1.964c-.012.012-.025.024-.039.036h-5.804c-.648,0-1.173.525-1.173,1.173v3.479c0,1.681,1.363,3.044,3.044,3.044h1.469c.8,3.582,3.998,6.269,7.817,6.269s7.016-2.687,7.816-6.269h13.642v-.002h3.321c.8,3.583,3.998,6.272,7.817,6.272s7.018-2.689,7.817-6.272h1.039c1.261,0,2.284-1.023,2.284-2.284v-15.789c0-.862-.205-1.711-.599-2.477ZM15.509,19.261h10.461v2s-10.462,0-10.462,0v-2ZM15.505,25.278h10.469v2s-10.47,0-10.47,0v-2ZM15.501,31.296h10.477v2s-10.478,0-10.478,0v-2ZM16.296,51.278c-3.316,0-6.015-2.699-6.015-6.018s2.698-6.015,6.015-6.015,6.014,2.698,6.014,6.015-2.698,6.018-6.014,6.018ZM21.648,39.313c-1.191-1.073-2.699-1.794-4.369-2h8.703v2s-4.334,0-4.334,0ZM42.146,17.099c0-.526.426-.952.952-.952h5.892c.53,0,1.02.282,1.286.741l3.831,8.64c.575.991-.14,2.232-1.286,2.232h-9.723c-.526,0-.952-.426-.952-.952v-9.709ZM48.894,51.278c-3.316,0-6.015-2.699-6.015-6.018s2.698-6.015,6.015-6.015,6.015,2.698,6.015,6.015-2.698,6.018-6.015,6.018ZM58.033,36.026h-3.104c-1.039,0-1.881-.842-1.881-1.881v-.854c0-1.039.842-1.881,1.881-1.881h3.104v4.615Z"/> <path d="M48.894,42.055c-1.771,0-3.207,1.437-3.207,3.207s1.436,3.208,3.207,3.208,3.207-1.437,3.207-3.208-1.435-3.207-3.207-3.207Z"/> <path d="M16.296,42.055c-1.771,0-3.207,1.437-3.207,3.207,0,1.771,1.436,3.208,3.207,3.208s3.207-1.437,3.207-3.208-1.435-3.207-3.207-3.207Z"/> </svg>',
  'forest': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M47.19,60h-2.57l-.14-5.76c-.01-.55-.49-.98-1.02-.98-.55.02-.99.48-.97,1.03l.13,5.71h-3.47l.64-9.81c.03-.55-.38-1.02-.94-1.06-.53-.02-1.02.38-1.06.93l-.64,9.94h-2.57c-.67,0-1.2-.59-1.12-1.26l1.43-12.09c4.81-.86,8.58-4.8,9.24-9.72.54-.14,1.07-.3,1.56-.5l2.62,22.31c.08.67-.45,1.26-1.12,1.26Z"/> <path d="M60,35.39c0,5.21-4.17,9.43-9.31,9.43h-2l-1.01-8.62c-.03-.25-.11-.47-.22-.68.41-.27.8-.55,1.13-.88.4-.38.41-1.01.03-1.41-.39-.4-1.02-.41-1.42-.03-.74.72-1.78,1.28-2.99,1.64-.14-3.25-1.65-6.22-4.08-8.25,1-1.59,1.54-3.44,1.54-5.37,0-4.72-3.23-8.7-7.63-9.74-.16-1.07-.47-2.09-.91-3.04,1.59-2.66,4.47-4.44,7.76-4.44,4.99,0,9.05,4.11,9.05,9.17,0,.02-.01.04-.01.06,4.19.21,7.51,3.7,7.51,7.99,0,2.29-.95,4.34-2.46,5.8,2.98,1.57,5.02,4.73,5.02,8.37Z"/> <path d="M30.513,58.525l-2.59-22.097c-1.435.569-3.09.891-4.818.891-1.711,0-3.351-.316-4.777-.874l-2.61,22.079c-.093.786.521,1.477,1.312,1.477h2.349l.64-9.94c.04-.55.52-.95,1.06-.93.56.04.97.51.94,1.06l-.64,9.81h3.47l-.13-5.71c-.02-.55.42-1.01.97-1.03.53,0,1.01.43,1.02.98l.14,5.76h2.351c.791,0,1.404-.69,1.312-1.475Z"/> <path d="M37.205,27.023c1.517-1.46,2.468-3.517,2.468-5.804,0-4.288-3.328-7.778-7.509-7.991,0-.02.003-.039.003-.059,0-5.064-4.053-9.169-9.052-9.169s-9.052,4.105-9.052,9.169c0,.02.003.039.003.059-4.181.213-7.509,3.703-7.509,7.991,0,2.287.951,4.345,2.468,5.804-2.984,1.571-5.025,4.724-5.025,8.366,0,5.208,4.168,9.429,9.309,9.429h2.015l1.017-8.609c.028-.238.107-.459.215-.665-.425-.275-.823-.57-1.166-.9-.398-.383-.41-1.016-.027-1.414.383-.398,1.017-.409,1.414-.027,1.376,1.324,3.742,2.115,6.328,2.115s4.951-.791,6.327-2.115c.398-.382,1.031-.371,1.414.027s.371,1.031-.027,1.414c-.333.32-.719.607-1.128.875.109.21.191.434.219.675l1.01,8.623h2.001c5.141,0,9.309-4.222,9.309-9.429,0-3.641-2.041-6.795-5.025-8.366Z"/> </svg>',
  'chainsaw': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path d="M36.61,37.61l-1.41,1.41,1.82,1.82c.19.2.45.29.71.29.25,0,.51-.09.7-.29.39-.39.39-1.02,0-1.41l-1.82-1.82Z"/> <path d="M40.71,33.51l-1.42,1.42,1.82,1.82c.2.19.45.29.71.29s.51-.1.71-.29c.39-.39.39-1.03,0-1.42l-1.82-1.82Z"/> <path d="M44.8,29.42l-1.41,1.41,1.82,1.82c.19.2.45.3.71.3.25,0,.51-.1.7-.3.39-.39.39-1.02,0-1.41l-1.82-1.82Z"/> <path d="M48.9,25.32l-1.42,1.42,1.82,1.82c.2.19.45.29.71.29.25,0,.51-.1.71-.29.39-.39.39-1.02,0-1.42l-1.82-1.82Z"/> <path d="M52.99,21.23l-1.41,1.41,1.82,1.82c.19.2.45.3.7.3.26,0,.52-.1.71-.3.39-.39.39-1.02,0-1.41l-1.82-1.82Z"/> <path d="M59.1,12.11h-.01l-2.83.02c-.272-.915-.72-1.788-1.333-2.574.004.005.009.009.012.014l1.89-1.89c.4-.39.4-1.02,0-1.41-.39-.39-1.02-.39-1.41,0l-1.89,1.89c.016.012.032.027.049.039-.856-.673-1.817-1.141-2.823-1.409.074.019.151.028.224.049l.01-2.83c0-.55-.44-1-.99-1h-.01c-.55,0-1,.44-1,.99l-.01,2.53c.005,0,.01.001.015.001-1.056-.035-2.117.138-3.116.526.021-.008.04-.02.061-.028l-1.17-2.38c-.25-.49-.84-.7-1.34-.46-.5.25-.7.85-.46,1.34l1.199,2.459c-.347.248-.682.519-.993.831l-1.298,1.298-1.818-1.828c-.39-.39-1.03-.39-1.42,0-.39.4-.39,1.03,0,1.42l1.823,1.823-2.68,2.68-1.823-1.823c-.39-.39-1.02-.39-1.41,0-.39.39-.39,1.02,0,1.41l1.823,1.823-2.68,2.68-1.823-1.823c-.39-.39-1.03-.39-1.42,0s-.39,1.03,0,1.42l1.823,1.823-2.68,2.68-1.823-1.823c-.39-.39-1.02-.39-1.41,0-.39.39-.39,1.02,0,1.41l1.823,1.823-2.68,2.68-1.823-1.823c-.39-.39-1.03-.39-1.42,0s-.39,1.03,0,1.42l1.823,1.823-1.157,1.157c.41-.012.672-.019.676-.019,1.258,0,2.439.489,3.328,1.378l.518.518,18.782-18.782c1.301-1.301,3.411-1.301,4.712,0s1.301,3.411,0,4.712l-18.782,18.782,3.107,3.107c.031.031.053.069.083.101l18.936-18.936c.328-.328.613-.681.871-1.048-.014.019-.023.04-.037.059l2.45,1.19c.14.07.29.11.44.11.37,0,.73-.21.9-.57.24-.49.04-1.09-.46-1.33l-2.38-1.17c-.003.008-.008.016-.011.024.378-.983.548-2.025.516-3.064l2.525-.02c.55,0,1-.45,1-1-.01-.55-.45-1-1-1ZM45.058,7.429c-.04.021-.077.047-.117.069.039-.022.077-.048.117-.069ZM50.068,6.639c-.065-.011-.129-.019-.194-.028.065.009.129.017.194.028ZM53.764,8.348c.18.148.359.305.526.472.032.032.056.069.088.101-.032-.033-.059-.069-.092-.102-.168-.168-.344-.322-.522-.472ZM55.615,18.151c.016-.03.036-.059.052-.089-.016.03-.036.059-.052.089ZM56.471,13.065c.007.042.012.085.018.128-.006-.042-.011-.085-.018-.128Z"/> <path d="M15.993,21.229h1.358c.977,0,1.77.793,1.77,1.77v23.508c0,.977-.793,1.769-1.769,1.769h-1.358c-.977,0-1.77-.793-1.77-1.77v-23.508c0-.977.793-1.769,1.769-1.769Z" transform="translate(-19.693 21.972) rotate(-45.007)"/> <path d="M25.516,31.843c-.527-.527-1.247-.813-1.992-.791l-4.142.121,8.747,8.746c1.469,1.47,1.469,3.861,0,5.33l-.961.961c-.712.712-1.659,1.104-2.666,1.104s-1.952-.392-2.664-1.103l-11.365-11.365-4.382,4.383c-1.582,1.583-1.582,4.148,0,5.731l8.304,8.302,1.319,5.535c.282,1.183,1.752,1.599,2.611.739l15.527-15.53c1.057-1.057,1.056-2.77,0-3.827l-8.337-8.336ZM19.44,52.086c-.195.195-.451.293-.707.293s-.512-.098-.707-.293l-2.295-2.295c-.391-.391-.391-1.023,0-1.414s1.023-.391,1.414,0l2.295,2.295c.391.391.391,1.023,0,1.414ZM22.094,49.432c-.195.195-.451.293-.707.293s-.512-.098-.707-.293l-2.294-2.294c-.391-.391-.391-1.023,0-1.414s1.023-.391,1.414,0l2.294,2.294c.391.391.391,1.023,0,1.414Z"/> </svg>',
  'stump': '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <ellipse cx="32" cy="8.414" rx="15.343" ry="4.412"/> <path d="M11.492,30.861c-.423-.362-1.065-.287-1.393.163l-3.563,4.899c-.346.476-.278,1.136.157,1.531l7.975,7.245v-11.459c-.734-.289-1.388-.846-1.388-.846l-1.789-1.533Z"/> <path d="M57.415,24.032l-3.437-4.726c-.369-.508-1.093-.592-1.57-.184l-1.689,1.448s-2.964,2.55-3.365-.426v-8.406c-1.26.882-2.999,1.512-4.859,1.962v21.944c0,.553-.447,1-1,1s-1-.447-1-1V14.114c-1.618.283-3.229.453-4.617.556v14.635c0,.553-.447,1-1,1s-1-.447-1-1v-14.521c-.912.036-1.585.042-1.878.042-1.378,0-11.065-.11-15.331-3.075v43.834c0,1.477,2.534,2.782,6.411,3.583v-15.578c0-.55.45-1,1-1s1,.45,1,1v15.928c1.426.208,2.98.353,4.62.424v-9.012c0-.55.45-1,1-1s1,.45,1,1v9.063c.105,0,.206.005.311.005,8.474,0,15.343-1.975,15.343-4.412v-20.914l9.891-8.986c.47-.427.543-1.14.17-1.654Z"/> </svg>',
}

GA_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Expletus+Sans:wght@600&display=swap" rel="stylesheet">'''

def head(title, desc, root='', leaflet=False):
    lf = ''
    if leaflet:
        lf = '''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{root}assets/img/capital-sawmill-logo.png">
{GA_FONTS}
{lf}
<link rel="stylesheet" href="{root}assets/css/main.css">
</head>
<body>'''

def header(root=''):
    return f'''
<header id="header">
  <div id="top-info">
    <div class="container">
      <div class="bar-inner">
        <div class="bar-item" id="estimate"><a id="estimate-modal-button" href="{root}contact/">Get A Free Estimate!</a></div>
        <div class="bar-item" id="top-phone"><a href="{PHONE_TEL}">{SVG_PHONE} {PHONE_DISPLAY}</a></div>
        <div class="bar-item" id="top-address"><a href="https://www.google.com/maps/place/Capital+Sawmill+Service,+Tree+Service+%26+More/data=!4m2!3m1!1s0x0:0xd58ee223ea17ec14?sa=X&amp;ved=1t:2428&amp;ictx=111" target="_blank" rel="noopener">{SVG_MARKER} {ADDRESS}</a></div>
      </div>
    </div>
  </div>

  <div id="main-menu">
    <div class="container">
      <div id="main-menu-container">
        <nav id="main-nav">
          <ul>
            <li>
              <a id="main-nav-home" href="{root}">Capital Sawmill&trade;</a>
              <div class="sub-menu">
                <ul>
                  <li><a href="{root}about/">About Us</a></li>
                  <li><a href="{root}#service-area-section">Who We Serve</a></li>
                  <li><a href="{root}firewood/">Firewood</a></li>
                </ul>
              </div>
            </li>
            <li>
              <a href="{root}wood-slabs/">Wood Slabs</a>
              <div id="nav-all-wood-slabs" class="sub-menu">
                <div id="nav-common-woods">
                  <p>Common</p>
                  <ul id="nav-common-woods-col1">
                    <li><a href="{root}wood-slabs/#walnut"><div class="nav-wood-sample ws-walnut"></div><p>Walnut</p></a></li>
                    <li><a href="{root}wood-slabs/#maple"><div class="nav-wood-sample ws-maple"></div><p>Maple</p></a></li>
                    <li><a href="{root}wood-slabs/#oak"><div class="nav-wood-sample ws-oak"></div><p>Oak</p></a></li>
                  </ul>
                  <ul id="nav-common-woods-col2">
                    <li><a href="{root}wood-slabs/#cherry"><div class="nav-wood-sample ws-cherry"></div><p>Cherry</p></a></li>
                    <li><a href="{root}wood-slabs/#pine"><div class="nav-wood-sample ws-pine"></div><p>Pine</p></a></li>
                  </ul>
                </div>
                <div id="nav-specialty-slabs">
                  <p>Specialty Slabs</p>
                  <ul>
                    <li><a href="{root}wood-slabs/#honey-locust">Honey Locust</a></li>
                    <li><a href="{root}wood-slabs/#sycamore">Sycamore</a></li>
                    <li><a href="{root}wood-slabs/#box-elder-maple">Box Elder Maple</a></li>
                    <li><a href="{root}wood-slabs/#catalpa">Catalpa</a></li>
                  </ul>
                </div>
              </div>
            </li>
            <li>
              <a href="{root}wood-products/">Wood Products</a>
              <div class="sub-menu">
                <ul>
                  <li><a href="{root}wood-products/#bartops">Bartops</a></li>
                  <li><a href="{root}wood-products/#table-tops">Table Tops</a></li>
                  <li><a href="{root}wood-products/#mantels">Mantels</a></li>
                  <li><a href="{root}wood-products/#deer-plaques">Deer Plaque Mounts</a></li>
                  <li><a href="{root}firewood/">Firewood</a></li>
                </ul>
              </div>
            </li>
            <li>
              <a href="{root}tree-removal/">Tree Removal</a>
            </li>
            <li id="header-contact-button"><a href="{root}contact/">Contact</a></li>
          </ul>
        </nav>
        <div id="capital-sawmill-logo"><a href="{root}"><img src="{root}assets/img/capital-sawmill-logo.png" width="144" height="80" alt="Capital Sawmill Service, LLC"></a></div>
        <div class="mobile-actions">
          <a id="mobile-call" href="{PHONE_TEL}" aria-label="Call Capital Sawmill">{SVG_PHONE}</a>
          <button id="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-drawer">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
      <div class="clear-float"></div>
    </div>
  </div>
</header>

<div id="drawer-overlay"></div>
<nav id="mobile-drawer" aria-label="Mobile menu">
  <div class="drawer-top">
    <a href="{root}"><img src="{root}assets/img/capital-sawmill-logo.png" width="104" height="58" alt="Capital Sawmill"></a>
    <button id="drawer-close" aria-label="Close menu">&times;</button>
  </div>
  <a class="drawer-estimate" href="{root}contact/">Get A Free Estimate!</a>
  <ul class="drawer-nav">
    <li><a href="{root}">Home</a></li>
    <li><a href="{root}tree-removal/">Tree Removal</a></li>
    <li class="has-sub">
      <div class="drawer-row">
        <a href="{root}wood-slabs/">Wood Slabs</a>
        <button class="sub-toggle" aria-expanded="false" aria-label="Show wood slab species">{SVG_CHEVRON}</button>
      </div>
      <ul class="drawer-sub">
        <li><a href="{root}wood-slabs/#walnut">Walnut</a></li>
        <li><a href="{root}wood-slabs/#maple">Maple</a></li>
        <li><a href="{root}wood-slabs/#oak">Oak</a></li>
        <li><a href="{root}wood-slabs/#cherry">Cherry</a></li>
        <li><a href="{root}wood-slabs/#pine">Pine</a></li>
        <li><a href="{root}wood-slabs/#honey-locust">Honey Locust</a></li>
        <li><a href="{root}wood-slabs/#sycamore">Sycamore</a></li>
        <li><a href="{root}wood-slabs/#box-elder-maple">Box Elder Maple</a></li>
        <li><a href="{root}wood-slabs/#catalpa">Catalpa</a></li>
      </ul>
    </li>
    <li class="has-sub">
      <div class="drawer-row">
        <a href="{root}wood-products/">Wood Products</a>
        <button class="sub-toggle" aria-expanded="false" aria-label="Show wood products">{SVG_CHEVRON}</button>
      </div>
      <ul class="drawer-sub">
        <li><a href="{root}wood-products/#bartops">Bar Tops</a></li>
        <li><a href="{root}wood-products/#table-tops">Table Tops</a></li>
        <li><a href="{root}wood-products/#mantels">Mantels</a></li>
        <li><a href="{root}wood-products/#deer-plaques">Deer Plaque Mounts</a></li>
        <li><a href="{root}wood-products/#chainsaw-signs">Chainsaw Signs</a></li>
      </ul>
    </li>
    <li><a href="{root}firewood/">Firewood</a></li>
    <li><a href="{root}about/">About Us</a></li>
    <li><a href="{root}contact/">Contact</a></li>
  </ul>
  <div class="drawer-contact">
    <a class="drawer-call" href="{PHONE_TEL}">{SVG_PHONE} {PHONE_DISPLAY}</a>
    <p><a class="drawer-addr" href="https://www.google.com/maps/place/Capital+Sawmill+Service,+Tree+Service+%26+More/data=!4m2!3m1!1s0x0:0xd58ee223ea17ec14?sa=X&amp;ved=1t:2428&amp;ictx=111" target="_blank" rel="noopener">4119 US Highway 20, Nassau, NY 12123</a><br>Monday &ndash; Saturday &middot; 8AM &ndash; 6PM</p>
  </div>
</nav>'''

def plank(text, small=False, alt=False, tag='h2', anchor='', icon=None, icon_after=False):
    cls = 'plank small' if small else 'plank'
    if alt: cls += ' alt'
    a = f' id="{anchor}"' if anchor else ''
    before, after = '', ''
    if icon and icon_after:
        after = f'<span class="plank-glyph after">{GLYPHS[icon]}</span>'
    elif icon:
        before = f'<span class="plank-glyph">{GLYPHS[icon]}</span>'
    return f'<div class="plank-wrap"{a}><div class="{cls}"><{tag}>{before}{text}{after}</{tag}></div></div>'

def footer(root=''):
    return f'''
<footer id="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img src="{root}assets/img/capital-sawmill-logo.png" width="144" height="80" alt="Capital Sawmill logo" style="margin-bottom:12px">
        <ul class="contact-info-list">
          <li><a href="{PHONE_TEL}">{SVG_PHONE} {PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{SVG_ENVELOPE} {EMAIL}</a></li>
          <li>{SVG_MARKER} 4119 US Highway 20, Nassau, NY 12123</li>
        </ul>
        <ul id="footer-social-links">
          <li><a href="https://www.facebook.com/CapitalSawmill" target="_blank" rel="noopener" aria-label="Facebook">{SVG_FB}</a></li>
          <li><a href="https://www.instagram.com/capitalsawmillservice" target="_blank" rel="noopener" aria-label="Instagram">{SVG_IG}</a></li>
          <li><a href="https://www.linkedin.com/company/capital-sawmill-service-llc" target="_blank" rel="noopener" aria-label="LinkedIn">{SVG_LI}</a></li>
        </ul>
      </div>
      <div>
        <h3>Come Visit Us</h3>
        <p>Monday &ndash; Saturday<br>8AM &ndash; 6PM</p>
        <h3>Explore</h3>
        <p style="line-height:2.1">
          <a href="{root}wood-slabs/">Wood Slabs</a><br>
          <a href="{root}wood-products/">Wood Products</a><br>
          <a href="{root}tree-removal/">Tree Removal</a><br>
          <a href="{root}firewood/">Firewood</a><br>
          <a href="{root}about/">About Us</a><br>
          <a href="{root}contact/">Contact</a>
        </p>
      </div>
      <div id="footer-map">
        <h3>Find the Mill</h3>
        <iframe title="Capital Sawmill location map" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d47035.36349320028!2d-73.69139819585202!3d42.54021004225813!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd58ee223ea17ec14!2sCapital+Sawmill+Service!5e0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy;2026 Capital Sawmill Service, LLC. All Rights Reserved.</span>
      <span><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    </div>
  </div>
</footer>

<div id="sticky-call"><a href="{PHONE_TEL}">{SVG_PHONE} CALL STEVE &mdash; {PHONE_DISPLAY}</a></div>

<script src="{root}assets/js/main.js"></script>
</body>
</html>'''

# ================= PAGE BODIES =================

def call_cta(center=True, dark=False):
    style = ' style="text-align:center;margin-top:34px"' if center else ''
    return f'''<div{style}>
      <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a>
      &nbsp; <a class="btn btn-light" href="/contact/">Get a Free Estimate</a>
    </div>'''

INDEX_BODY = f'''
<section id="hero">
  <video autoplay muted loop playsinline poster="assets/img/hero-poster.jpg">
    <source src="assets/vid/header.mp4" type="video/mp4">
  </video>
  <div class="hero-shade"></div>
  <div class="hero-badge">
    <svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M466.5 83.7l-192-80a48.15 48.15 0 0 0-36.9 0l-192 80C27.7 91.1 16 108.6 16 128c0 198.5 114.5 335.7 221.5 380.3 11.8 4.9 25.1 4.9 36.9 0C360.1 472.6 496 349.3 496 128c0-19.4-11.7-36.9-29.5-44.3zM256.1 446.3l-.1-381 175.9 73.3c-3.3 151.4-82.1 261.1-175.8 307.7z"/></svg>
    <span>Licensed<br>&amp; Insured</span>
  </div>
  <div class="hero-copy">
    <h1>Albany NY Region<br>Tree and Sawmill Service</h1>
    <p class="hero-sub">Two full trades under one roof in the Capital Region &mdash; take-downs of any size, slabs up to 30&Prime; wide. And when you want, we&rsquo;ll take your tree the whole journey.</p>
    <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a>
    &nbsp; <a class="btn btn-light" href="contact/">Get a Free Estimate</a>
  </div>
</section>

<section class="section section-cream" id="two-trades">
  <div class="container">
    <div class="page-split split-tree">
      <div class="page-split-col split-major">
        {plank('Residential &amp; Commercial Tree Services')}
        <img class="split-photo-inline" src="assets/img/07-14-009.jpg" alt="Tree removal in progress" loading="lazy">
        <p>With over 30 years of experience, our tree experts trim or remove trees of any size that are unwanted or problematic. We handle all facets of tree care &mdash; removal, pruning, stump grinding, lacing, thinning, and crown reduction &mdash; and we get the job done in a timely fashion, leaving the place looking great.</p>
        <p>Our licensed and insured arborists have been doing tree work for decades, so there truly is no job too big to handle. Proper tree care is an investment that can lead to substantial returns &mdash; well-cared-for trees are attractive and add considerable value to your property, while poorly maintained trees can be a significant liability.</p>
        <p>Pruning or removing trees, especially large ones, is dangerous work that should be done only by those trained and equipped to work safely in trees. From emergency storm-damage cleanup to routine tree trimming, we serve homeowners and businesses across Albany, Rensselaer, and Columbia counties &mdash; East Greenbush, Troy, Schenectady, Chatham, Nassau, and the rest of the Capital Region. Call now for a free consultation and make us your tree service!</p>
        <div class="service-tiles">
          <a class="service-tile" href="tree-removal/"><img src="assets/img/100_0254-1.jpg" alt="Bucket truck tree removal" loading="lazy"><span>Tree Removal</span></a>
          <a class="service-tile" href="tree-removal/"><img src="assets/img/tree-pruning.jpg" alt="Tree pruning" loading="lazy"><span>Tree Pruning</span></a>
          <a class="service-tile" href="tree-removal/"><img src="assets/img/land-clearing.jpg" alt="Land clearing" loading="lazy"><span>Land Clearing</span></a>
          <a class="service-tile" href="tree-removal/"><img src="assets/img/stump-grinding.jpg" alt="Stump grinding" loading="lazy"><span>Stump Grinding</span></a>
          <a class="service-tile" href="tree-removal/"><img src="assets/img/wood-chipping.jpg" alt="Wood chipping" loading="lazy"><span>Wood Chipping</span></a>
          <a class="service-tile" href="tree-removal/"><img src="assets/img/debris-removal.jpg" alt="Debris removal" loading="lazy"><span>Debris Removal</span></a>
        </div>
        <p class="split-cta"><a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a> <a class="btn btn-light" href="tree-removal/">Explore Tree Services</a></p>
      </div>
      <div class="page-split-col split-minor">
        {plank('From Your Tree to Your Table', small=True)}
        <div class="process">
          <div class="process-step">
            <div class="step-badge"><img src="assets/img/step-takedown.png" alt="" width="58" height="58"><span class="step-num">1</span></div>
            <div class="step-body">
              <h4>We Take It Down</h4>
              <p>Licensed, insured, and equipped for trees of any size &mdash; problematic or just in the way.</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-badge"><img src="assets/img/step-mill.png" alt="" width="58" height="58"><span class="step-num">2</span></div>
            <div class="step-body">
              <h4>We Mill It</h4>
              <p>On location with our portable band sawmill, or on the stationary mill at our shop in Nassau.</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-badge"><img src="assets/img/step-keep.png" alt="" width="58" height="58"><span class="step-num">3</span></div>
            <div class="step-body">
              <h4>You Keep It</h4>
              <p>Your tree comes back as slabs, beams, or a finished piece &mdash; lumber with a story you already know.</p>
            </div>
          </div>
        </div>
        <button id="video-open" class="video-thumb" aria-label="Watch: How Problematic Trees are Turned into Custom Lumber">
          <img src="assets/img/video-thumb.jpg" alt="Tree felling in action" loading="lazy">
          <span class="video-play" aria-hidden="true"><svg viewBox="0 0 448 512" fill="currentColor"><path d="M424.4 214.7L72.4 6.6C43.8-10.3 0 6.1 0 47.9V464c0 37.5 40.7 60.1 72.4 41.3l352-208c31.4-18.5 31.5-64.1 0-82.6z"/></svg></span>
          <span class="video-thumb-label">Watch How It&rsquo;s Done</span>
        </button>
      </div>
    </div>
  </div>
</section>

<div id="video-modal" hidden>
  <div class="video-modal-backdrop"></div>
  <div class="video-modal-box">
    <button id="video-close" aria-label="Close video">&times;</button>
    <div class="video-embed">
      <iframe id="video-frame" title="How Problematic Trees are Turned into Custom Lumber" data-src="https://www.youtube-nocookie.com/embed/0YnnWF1ilhc?autoplay=1" src="about:blank" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
</div>

<div class="grain-divider"></div>

<section class="section section-cream" id="sawmill-products">
  <div class="container">
    <div class="page-split split-tree">
      <div class="page-split-col split-major">
        {plank('Sawmill Services &amp; Wood Products')}
        <p>We mill custom lumber for bar tops, tables, counters, mantels, and much more &mdash; live-edge slabs up to 30&Prime; wide, air-dried under cover for up to two years. Milling on location with our portable band sawmill, or at the mill in Nassau. Slabs and finished pieces ship nationwide.</p>
        <p>Our shop southeast of Albany stocks live-edge walnut, cherry, maple, oak, and pine slabs for sale, plus specialty hardwoods like honey locust, sycamore, box elder, and catalpa &mdash; one-of-a-kind boards you won&rsquo;t find at a lumber yard.</p>
        <div class="service-tiles">
          <a class="service-tile" href="wood-slabs/"><img src="assets/img/milling-on-site.jpg" alt="Milling on site" loading="lazy"><span>Custom Milling</span></a>
          <a class="service-tile" href="wood-slabs/"><img src="assets/img/wood-slabs-on-forklift.jpg" alt="Live-edge wood slabs" loading="lazy"><span>Live-Edge Slabs</span></a>
          <a class="service-tile" href="wood-products/#bartops"><img src="assets/img/wp-bartops.jpg" alt="Bar tops" loading="lazy"><span>Bar Tops</span></a>
          <a class="service-tile" href="wood-products/#table-tops"><img src="assets/img/wp-table-tops.jpg" alt="Table tops" loading="lazy"><span>Table Tops</span></a>
          <a class="service-tile" href="wood-products/#mantels"><img src="assets/img/wp-mantels.jpg" alt="Fireplace mantels" loading="lazy"><span>Mantels</span></a>
          <a class="service-tile" href="wood-products/#deer-plaques"><img src="assets/img/wp-dpm.jpg" alt="Deer plaque mounts" loading="lazy"><span>Deer Plaques</span></a>
        </div>
        <p class="split-cta"><a class="btn btn-maroon" href="wood-slabs/">Buy Wood Slabs</a> <a class="btn btn-call" href="wood-products/">Browse Wood Products</a></p>
      </div>
      <div class="page-split-col split-minor">
        {plank('Firewood', small=True, icon='firewood', icon_after=True)}
        <img class="split-photo" src="assets/img/wp-firewood.jpg" alt="Seasoned firewood" loading="lazy">
        <p>Seasoned hardwood firewood for sale in Nassau NY &mdash; stored clean and dry under our pavilion, sold by the face cord, and delivered across the Capital Region. Camp wood, kindling kegs, and smoker chunks too.</p>
        <p class="split-cta"><a class="btn btn-call" href="firewood/">Firewood Pricing &amp; Availability</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section-map-full" id="service-area-section">
  <div class="map-full-wrap">
    <div id="service-map"></div>
    <div class="map-overlay-title"><h2>Service<br>Area</h2></div>
    <div class="town-chips">
      <span>Albany</span><span>Chatham</span><span>Rensselaer</span><span>Columbia</span><span>Schenectady</span><span>East Greenbush</span><span>Troy</span><span>Cohoes</span><span>Latham</span><span>Colonie</span><span>Westmere</span><span>Delmar</span><span>Wynantskill</span><span>Westerlo</span><span>Rotterdam</span><span>New Lebanon</span><span>Ghent</span><span>Petersburg</span>
    </div>
  </div>
</section>

<section class="testimonial-stage" id="testimonials">
  <video class="testimonial-bg" autoplay muted loop playsinline preload="metadata" poster="assets/img/testimonials-poster.jpg" aria-hidden="true">
    <source src="assets/vid/testimonials-bg.mp4" type="video/mp4">
  </video>
  <div class="testimonial-shade"></div>
  <div class="container testimonial-inner">
    {plank('What Neighbors Say')}
    <div class="testimonials">
      <blockquote class="testimonial">
        <span class="t-stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        I want to thank you again for your prompt and very professional response to our tree problem. I was home and was able to see the tree removal process and the clean-up as well. All of you are a real credit to your business. Neither my wife nor I will hesitate to call upon you again.
        <cite>John Walden</cite>
      </blockquote>
      <blockquote class="testimonial">
        <span class="t-stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        Capital Sawmill has done tree work for us at 3 different times. We needed tree and stump removal and extensive trimming on very old, large maples. Steve and his crew did a terrific job. The entire team was very pleasant, the price was fair and the crew cleaned the area of all brush. I would recommend Capital Sawmill very highly.
        <cite>Mary LaFleur</cite>
      </blockquote>
      <blockquote class="testimonial">
        <span class="t-stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        I would like to thank you again for the amazing job you did at our house. We appreciate that you were able to come so quickly &mdash; it was comforting to know TRUE professionals were on the job! Thanks again!
        <cite>Billy Lauritsen</cite>
      </blockquote>
    </div>
    <p class="testimonial-cta"><a class="btn btn-call" href="https://www.google.com/maps/place/Capital+Sawmill+Service,+Tree+Service+%26+More/data=!4m2!3m1!1s0x0:0xd58ee223ea17ec14?sa=X&amp;ved=1t:2428&amp;ictx=111" target="_blank" rel="noopener">Read More Reviews on Google</a></p>
  </div>
</section>

<section class="section section-faq" id="faq-section">
  <div class="container">
    {plank('Frequently Asked Questions', alt=True)}
    <div class="faq">
      <details>
        <summary>Do you remove valuable wood in exchange for the lumber?</summary>
        <div class="faq-a">Unfortunately no. The high cost of vehicles, machinery, labor, insurance, and fuel to cut and process the wood versus the value of the wood itself doesn&rsquo;t enable us to do that.</div>
      </details>
      <details>
        <summary>Do you carry common building-supply wood like 2x4&rsquo;s?</summary>
        <div class="faq-a">We cut larger wood specific for custom needs. Common building-supply wood can and should be purchased cheaper through stores like Home Depot and Lowes due to their mass production of it.</div>
      </details>
      <details>
        <summary>Can you turn MY tree into lumber I keep?</summary>
        <div class="faq-a">Yes &mdash; that&rsquo;s our specialty. We can take down your tree and mill it on site with our portable band sawmill, or bring it back to our stationary mill in Nassau. You end up with slabs, beams, or a finished piece from a tree you already own. Call us and tell us about the tree.</div>
      </details>
    </div>
  </div>
</section>

<section class="section section-dark" id="contact-section">
  <div class="container">
    {plank('The Fastest Way to Reach Us? Call.')}
    <div class="contact-grid">
      <div class="call-panel">
        <p style="max-width:520px;margin:0 auto">Steve answers his phone, not his inbox. For estimates, slab availability, or a straight answer about your tree &mdash; call.</p>
        <a class="big-phone" href="{PHONE_TEL}">{SVG_PHONE.replace('<svg ', '<svg style="width:30px;height:30px;margin-right:14px" ')}{PHONE_DISPLAY}</a>
        <p class="call-note">Monday &ndash; Saturday, 8AM &ndash; 6PM &middot; Nassau, NY</p>
      </div>
      <div>
        <h3 style="font-family:'Lato',sans-serif;text-transform:uppercase;letter-spacing:2px;color:var(--green-dark)">Rather write it down?</h3>
        <form id="estimate-form" class="contact-form" action="https://formsubmit.co/{EMAIL}" method="POST">
          <input type="hidden" name="_subject" value="New estimate request from capitalsawmill.com">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Full Name*" required>
          <input type="email" name="email" placeholder="Email*" required>
          <input type="tel" name="phone" placeholder="Phone (so we can call you back)">
          <textarea name="message" placeholder="Tell us about your tree or your project&hellip;"></textarea>
          <button class="btn btn-maroon" type="submit">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>
'''

TREE_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/07-14-009.jpg)">
  <h1>Tree Removal</h1>
  <p>Our licensed and insured arborists remove trees of any size that are unwanted or problematic.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call for a Free Estimate</a>
</section>

<section class="section">
  <div class="container">
    <p style="max-width:860px;margin:0 auto;text-align:center;font-size:19px">The people of Capital Sawmill have been doing tree work for decades, so there truly is no job too big to handle. You can count on us to get the job done in a timely fashion and leave the place looking great. Call now for a free consultation and make us your tree service!</p>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Tree Services')}
    <div class="service-tiles">
      <div class="service-tile"><img src="../assets/img/tree-pruning.jpg" alt="Tree pruning" loading="lazy"><span>Tree Pruning</span></div>
      <div class="service-tile"><img src="../assets/img/land-clearing.jpg" alt="Land clearing" loading="lazy"><span>Land Clearing</span></div>
      <div class="service-tile"><img src="../assets/img/stump-grinding.jpg" alt="Stump grinding" loading="lazy"><span>Stump Grinding</span></div>
      <div class="service-tile"><img src="../assets/img/milling-on-site.jpg" alt="Milling on site" loading="lazy"><span>Milling on Site</span></div>
      <div class="service-tile"><img src="../assets/img/wood-chipping.jpg" alt="Wood chipping" loading="lazy"><span>Wood Chipping</span></div>
      <div class="service-tile"><img src="../assets/img/debris-removal.jpg" alt="Debris removal" loading="lazy"><span>Debris Removal</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {plank('Why Hire an Arborist?', alt=True)}
    <div class="split">
      <div>
        <p>An arborist is a specialist in the care of individual trees. Arborists are knowledgeable about the needs of trees and are trained and equipped to provide proper care. Hiring an arborist is a decision that should not be taken lightly.</p>
        <p>Proper tree care is an investment that can lead to substantial returns. Well-cared-for trees are attractive and can add considerable value to your property. Poorly maintained trees can be a significant liability. Pruning or removing trees, especially large trees, can be dangerous work &mdash; it should be done only by those trained and equipped to work safely in trees.</p>
      </div>
      <div class="split-img"><img src="../assets/img/tree-pruning.jpg" alt="Arborist pruning a tree" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-dark">
  <div class="container">
    {plank("Don&rsquo;t Chip It &mdash; Keep It")}
    <div class="split">
      <div class="split-img"><img src="../assets/img/milling-on-site.jpg" alt="Milling a removed tree on site" loading="lazy"></div>
      <div>
        <p><strong>Here&rsquo;s the part most tree services can&rsquo;t offer:</strong> before your tree hits the chipper, ask us about milling it. Our portable band sawmill turns take-downs into usable lumber right in your yard &mdash; or we bring the log back to our mill. That maple shading your porch for 40 years could be your dining table for the next 40.</p>
        <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Ask About Milling Your Tree</a>
      </div>
    </div>
  </div>
</section>
'''

def species_card(anchor, name, img, body, sprite=None, strip=False):
    if img:
        thumb = f'<img src="../assets/img/{img}" alt="{name} wood" loading="lazy">'
    elif sprite:
        thumb = f'<img src="../assets/img/{sprite}" alt="{name} wood sample" loading="lazy" style="height:130px">'
    else:
        thumb = '<div style="height:26px;background:url(../assets/tex/h2-bg.jpg);background-size:600px 120px;box-shadow:inset 0 -3px 6px rgba(0,0,0,.25)"></div>'
    return f'''<div class="card" id="{anchor}">
      {thumb}
      <div class="card-body">
        <h3>{name}</h3>
        {body}
      </div>
    </div>'''

SLABS_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/wood-slabs-on-forklift.jpg)">
  <h1>Custom Wood Slabs</h1>
  <p>One of a kind. Unfinished or finished, up to 30&Prime; wide &mdash; for whatever project you&rsquo;re working on.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Tell Us About Your Project</a>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p>We can mill trees at your site or ours with our portable band sawmill. We can take down your trees and mill them, or mill trees that have already been felled. Although we don&rsquo;t stock dimensional lumber, we can custom cut logs into planks of many widths and lengths, suited to fit your project &mdash; boards, beams, planks, posts, timbers, you name it.</p>
        <p>At our shop we have many woods available: free-form mantel pieces and bar tops in stock or cut to order, fireplace mantels in cherry, walnut, maple, oak, pine and more &mdash; with the natural wane of the wood or cut with square or rounded edges. Custom designed, hand-built furniture too. Call for rates, local or out-of-state.</p>
      </div>
      <div class="split-img"><img src="../assets/img/IMG_0446.jpg" alt="Stacked live-edge slabs" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Which Wood Is Right for You?')}
    <div class="species-grid">
      {species_card('walnut', 'Walnut', 'finished-walnut-slab.jpg',
        '<p>A straight-grained hardwood ranging from chocolate brown to blond. A top pick for headboards, antique-style dining tables, and mantels &mdash; typically clear-coated or oiled to bring out its color.</p><p class="pros"><strong>Pros:</strong> Very strong and stable; takes intricate carving; beautiful color.</p><p class="cons"><strong>Cons:</strong> One of the more costly woods; color varies board to board.</p>')}
      {species_card('cherry', 'Cherry', 'cherry-finished2.jpg',
        '<p>A fine, straight-grained hardwood from reddish brown to blond. Seen in carved chairs and clean-lined Shaker tables and cabinets alike.</p><p class="pros"><strong>Pros:</strong> Easily shaped, polishes well, rich unstained color.</p><p class="cons"><strong>Cons:</strong> Pricier; color can darken with age.</p>')}
      {species_card('maple', 'Maple', None,
        '<p>A creamy white hardwood, sometimes with a reddish tinge. One of the hardest species &mdash; the pick for heavy-use pieces like dressers and kitchen cabinets.</p><p class="pros"><strong>Pros:</strong> Affordable, ultra-durable, takes dark stains well.</p><p class="cons"><strong>Cons:</strong> Needs proper sealing before staining or it can blotch.</p>', sprite='sample-maple.jpg')}
      {species_card('oak', 'Oak', None,
        '<p>A very grainy hardwood in red and white varieties &mdash; the classic Arts &amp; Crafts and Mission-style wood with a distinctive wavy grain.</p><p class="pros"><strong>Pros:</strong> Very durable, resists warping, a clear finish highlights the grain beautifully.</p><p class="cons"><strong>Cons:</strong> Heavy stain can exaggerate the grain into a two-toned look.</p>', sprite='sample-oak.jpg')}
      {species_card('pine', 'Pine', None,
        '<p>An inexpensive, lightweight wood, yellowish or whitish with brown knots &mdash; the farmhouse-table classic.</p><p class="pros"><strong>Pros:</strong> Low cost, takes paint well, develops a rustic patina, resists shrinking and swelling.</p><p class="cons"><strong>Cons:</strong> Softwood &mdash; prone to scratches and dents.</p>', sprite='sample-pine.jpg')}
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    {plank('Specialty Slabs', alt=True)}
    <p style="text-align:center;max-width:800px;margin:0 auto 34px">We start with carefully selected logs from upstate New York. Lumber is stored under cover as it slowly air dries for up to two years &mdash; besides good logs, proper drying is the most important step in quality control.</p>
    <div class="species-grid">
      {species_card('honey-locust', 'Honey Locust', None,
        '<p>High quality, durable wood that polishes beautifully. Honey locust doesn&rsquo;t grow in numbers that support bulk industry &mdash; which is exactly why a slab of it is special. Also prized for posts and rails thanks to its dense, rot-resistant nature.</p>')}
      {species_card('sycamore', 'Sycamore', None,
        '<p>American Sycamore is the largest hardwood species in North America, yielding lumber with very respectable dimensions. Properly seasoned, it shows up in cabinets, butcher blocks, and barrels &mdash; quarter and rift sawn boards are especially stable and figured.</p>')}
      {species_card('box-elder-maple', 'Box Elder Maple', 'box-elder-unfinished.jpg',
        '<p>A light wood that lends itself well to furniture projects. Spalted boxelder, with its raspberry streaks, is highly prized for accent work and turnings.</p>')}
      {species_card('catalpa', 'Catalpa', 'catalpa-finished.jpg',
        '<p>Heartwood ranges from grayish tan to a rich golden brown with a straight, open grain that resembles ash. Rated durable for decay resistance &mdash; a great choice that&rsquo;s hard to find at a lumber yard.</p>')}
    </div>
    {call_cta()}
  </div>
</section>
'''

def product_section(anchor, title, img, body, dark=False, flip=False):
    cls = 'section section-dark' if dark else 'section section-cream'
    img_html = f'<div class="split-img"><img src="../assets/img/{img}" alt="{title}" loading="lazy" data-parallax="0.04"></div>'
    text_html = f'<div>{body}<p><a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Ask About Our Current Selection</a></p></div>'
    inner = (img_html + text_html) if not flip else (text_html + img_html)
    return f'''<section class="{cls}" id="{anchor}">
  <div class="container">
    {plank(title, alt=dark)}
    <div class="split">{inner}</div>
  </div>
</section>'''

PRODUCTS_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/wp-bartops.jpg)">
  <h1>Wood Products</h1>
  <p>Besides wood slabs and lumber, we build and sell a variety of wood products for your project needs.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call About a Custom Piece</a>
</section>

{product_section('bartops', 'Bar Tops', 'wp-bartops.jpg',
  '<p>High quality bar tops for bars, restaurants and homes &mdash; finished, or unfinished slabs for builders and woodworkers. We specialize in customization and build to standards that stand up to the passage of time and excessive use. Our unique, durable bar tops ship to customers across the United States.</p>')}

{product_section('table-tops', 'Table Tops', 'wp-table-tops.jpg',
  '<p>Choose the type and shape of wood from the many we have available &mdash; durable table tops made your way, at an affordable price. Compatible with all kinds of bases: stylish metal brackets, A-racks, legs with rollers, whatever your build calls for. Finished or unfinished.</p>', dark=True, flip=True)}

{product_section('mantels', 'Fireplace Mantels', 'wp-mantels.jpg',
  '<p>Beautiful wooden fireplace mantels, made to your taste &mdash; plain or extravagant, classic, modern, Victorian or colonial. Available in cherry, walnut, maple, oak, pine and more, with the natural live edge of the wood or cut square. Easy to mount and assemble, shipped across the United States.</p>')}

{product_section('deer-plaques', 'Deer Plaque Mounts', 'wp-dpm.jpg',
  '<p>Looking for a befitting mount for your trophy? We specialize in deer mount plaques with lots of selection &mdash; cedar, walnut, oak, pine, and many more. Customized plaques at a very reasonable price. It will look great on any wall.</p>', dark=True, flip=True)}

{product_section('chainsaw-signs', 'Chainsaw Signs', 'wp-chainsaw-signs.jpg',
  '<p>Hand-carved chainsaw signs, custom made from our own lumber &mdash; a one-of-a-kind marker for your camp, home, or business.</p>')}

<section class="section section-dark" id="firewood-link">
  <div class="container" style="text-align:center">
    {plank('Firewood', alt=True)}
    <p style="max-width:700px;margin:0 auto 24px">Seasoned mixed hardwoods by the face cord, kindling kegs, and smoker chunks in pear, apple, hickory and cherry.</p>
    <a class="btn btn-call" href="../firewood/">Firewood Pricing &amp; Availability</a>
  </div>
</section>
'''

FIREWOOD_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/wp-firewood.jpg)">
  <h1>Firewood For Sale</h1>
  <p>We know first-hand that New York gets COLD. Keep your home nice and cozy by stocking up on firewood.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call to Order</a>
</section>

<section class="section">
  <div class="container">
    {plank('Firewood Prices')}
    <div class="split">
      <div>
        <p>Seasoned mixed hardwoods, cut to stove lengths of 14&Prime; to 16&Prime; and stored under a pavilion so your wood stays clean and dry. Sold in face cord increments, priced for local delivery:</p>
        <ul style="line-height:2.2;font-size:18px">
          <li><strong>$230</strong> &mdash; face cord (4x8, one tier), dumped</li>
          <li><strong>$385</strong> &mdash; double face cord (4x8, two tiers), dumped</li>
          <li><strong>$540</strong> &mdash; triple face cord (4x8, three tiers), dumped</li>
        </ul>
        <p><strong>Kindling kegs</strong> &mdash; 11&Prime; diameter, 14&Prime; long, with a convenient carrying handle &mdash; are <strong>$15</strong> and make starting a fire a snap.</p>
      </div>
      <div class="split-img"><img src="../assets/img/FW-pavillion-3.jpg" alt="Firewood stored under the pavilion" loading="lazy" data-parallax="0.04"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Smoker Wood &amp; Camp Wood', alt=True)}
    <p style="max-width:800px;margin:0 auto;text-align:center">Smoker chunks in <strong>pear, apple, hickory and cherry</strong> for $14.95 a bag (about 14&Prime; x 14&Prime;), and smoker shavings in cherry and cherry/maple for $4.95 (14&Prime; x 20&Prime;). Camp wood available too &mdash; call ahead and we&rsquo;ll have it ready.</p>
    {call_cta()}
  </div>
</section>
'''

ABOUT_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/history-pics.jpg);background-position:center">
  <h1>About Capital Sawmill</h1>
  <p>Three generations of tree work &mdash; and a sawmill that gives good trees a second life.</p>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p>Capital Sawmill can take down your unwanted trees, prune for more light and healthier trees, and mill take-downs into lumber on site. Owner and arborist <strong>Steven Daniels</strong> has been providing tree service for over 30 years. In 1995 he added a portable sawmill to the company to better utilize the trees removed &mdash; and the rest is history.</p>
        <p>Capital Sawmill is located southeast of Albany at 4119 US Route 20 in Nassau, and previously operated as Steven Daniels Tree Service in Westchester, New York.</p>
        {call_cta(center=False)}
      </div>
      <div class="split-img"><img src="../assets/img/100_0254-1.jpg" alt="Capital Sawmill at work" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Company History')}
    <p style="max-width:800px;margin:0 auto 26px;text-align:center">It started with <strong>Frank Daniels</strong>, Steven&rsquo;s father, running his log truck in 1981. Steven grew up in the trade &mdash; pictured in front of his own log truck in 1991, and quite the climber, going out on a limb in 1992.</p>
    <img src="../assets/img/history-pics.jpg" alt="Daniels family tree service history photos, 1981-1992" style="display:block;margin:0 auto" loading="lazy">
  </div>
</section>
'''

CONTACT_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/tex/footer-bg.jpg)">
  <h1>Contact Capital Sawmill</h1>
  <p>Estimates are free. Answers are fast &mdash; especially by phone.</p>
</section>

<section class="section section-dark">
  <div class="container">
    {plank('Call First. Seriously.')}
    <div class="call-panel">
      <p style="max-width:640px;margin:0 auto">Steve runs the mill and the crew from his truck, not a desk. A two-minute call gets you an answer that three emails won&rsquo;t.</p>
      <a class="big-phone" href="{PHONE_TEL}">{SVG_PHONE.replace('<svg ', '<svg style="width:30px;height:30px;margin-right:14px" ')}{PHONE_DISPLAY}</a>
      <p class="call-note">Monday &ndash; Saturday, 8AM &ndash; 6PM &middot; Nassau, NY</p>
    </div>
    <div class="contact-grid">
      <div>
        <h3 style="font-family:'Lato',sans-serif;text-transform:uppercase;letter-spacing:2px;color:var(--green-dark)">Rather write it down?</h3>
        <form id="estimate-form" class="contact-form" action="https://formsubmit.co/{EMAIL}" method="POST">
          <input type="hidden" name="_subject" value="New estimate request from capitalsawmill.com">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Full Name*" required>
          <input type="email" name="email" placeholder="Email*" required>
          <input type="tel" name="phone" placeholder="Phone (so we can call you back)">
          <textarea name="message" placeholder="Tell us about your tree or your project&hellip;"></textarea>
          <button class="btn btn-maroon" type="submit">Send Message</button>
        </form>
      </div>
      <div>
        <h3 style="font-family:'Lato',sans-serif;text-transform:uppercase;letter-spacing:2px;color:var(--green-dark)">Visit the mill</h3>
        <ul class="contact-info-list">
          <li>{SVG_MARKER} 4119 US Highway 20, Nassau, NY 12123</li>
          <li>{SVG_CLOCK} Monday &ndash; Saturday, 8AM &ndash; 6PM</li>
          <li>{SVG_ENVELOPE} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <p style="margin-top:18px">Slabs are best picked in person &mdash; come walk the racks and find yours.</p>
      </div>
    </div>
  </div>
</section>
'''

THANKS_BODY = f'''
<section class="section" style="min-height:50vh;display:flex;align-items:center">
  <div class="container" style="text-align:center">
    {plank('Message Sent!')}
    <p style="max-width:600px;margin:0 auto 26px">Thanks &mdash; your message is on its way to Steve. Want an answer faster? You know what to do:</p>
    <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a>
  </div>
</section>
'''

PAGES = [
    # (path, title, description, body, root, leaflet)
    ('index.html',
     'Albany NY Custom Lumber, Wood Slabs, and Tree Removal | Capital Sawmill',
     'Capital Sawmill Service: expert tree removal and custom sawmilling in the Capital Region. We turn problem trees into beautiful lumber. Call (518) 479-0729.',
     INDEX_BODY, '', True),
    ('tree-removal/index.html',
     'Tree Removal & Tree Services | Capital Sawmill, Albany NY',
     'Licensed, insured tree removal, pruning, stump grinding and land clearing in the Albany Capital Region. 30+ years of experience. Call (518) 479-0729.',
     TREE_BODY, '../', False),
    ('wood-slabs/index.html',
     'Custom Wood Slabs — Walnut, Cherry, Maple, Oak & More | Capital Sawmill',
     'One-of-a-kind live-edge wood slabs up to 30" wide, air dried and milled in Nassau NY. Walnut, cherry, maple, oak, pine and specialty species. Ships nationwide.',
     SLABS_BODY, '../', False),
    ('wood-products/index.html',
     'Wood Products — Bar Tops, Table Tops, Mantels | Capital Sawmill',
     'Custom bar tops, table tops, fireplace mantels, deer plaque mounts and chainsaw signs, handmade from our own lumber in Nassau NY. Ships nationwide.',
     PRODUCTS_BODY, '../', False),
    ('firewood/index.html',
     'Firewood For Sale — Seasoned Hardwood | Capital Sawmill, Nassau NY',
     'Seasoned mixed hardwood firewood by the face cord, kindling kegs, and smoker chunks. Local delivery in the Capital Region. Call (518) 479-0729 to order.',
     FIREWOOD_BODY, '../', False),
    ('about/index.html',
     'About Us — Three Generations of Tree Work | Capital Sawmill',
     'Owner and arborist Steven Daniels has provided tree service for over 30 years, adding a sawmill in 1995 to give removed trees a second life as custom lumber.',
     ABOUT_BODY, '../', False),
    ('contact/index.html',
     'Contact Capital Sawmill — Call (518) 479-0729',
     'Free estimates for tree removal and custom milling. Call (518) 479-0729, Monday-Saturday 8AM-6PM, or visit the mill at 4119 US Highway 20, Nassau NY.',
     CONTACT_BODY, '../', False),
    ('thanks/index.html',
     'Thanks! | Capital Sawmill',
     'Your message is on its way to Capital Sawmill.',
     THANKS_BODY, '../', False),
]

for path, title, desc, body, root, leaflet in PAGES:
    out = SITE / path
    out.parent.mkdir(parents=True, exist_ok=True)
    html = head(title, desc, root, leaflet) + header(root) + '<main>' + body + '</main>' + footer(root)
    out.write_text(html)
    print(f'built {path} ({len(html)} bytes)')

print('done')
